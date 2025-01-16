#!/usr/bin/env python3
import struct
import sys
import os
import crcmod.predefined
from scapy.utils import PcapNgReader
from scapy.layers.inet import IP, TCP
from scapy.packet import Raw
from datetime import datetime
from google.protobuf import symbol_database
from google.protobuf import json_format

from protobuf import (
    AppGetHistED_pb2,
    AppGetHistPower_pb2,
    APPHeartbeatPB_pb2,
    APPInfomationData_pb2,
    AutoSearch_pb2,
    CommandPB_pb2,
    DevConfig_pb2,
    GetConfig_pb2,
    GPSTData_pb2,
    InfomationData_pb2,
    NetworkInfo_pb2,
    RealData_pb2,
    RealDataNew_pb2,
    SetConfig_pb2,
    WarnData_pb2,
)

commands = {
    0x2201: 'InfoDataReq', 0x2301: 'InfoDataRes',
    0x2202: 'HBReq', 0x2302: 'HBRes',
    0x2203: 'RealDataReq', 0x2303: 'RealDataRes',
    0x2204: 'RealDataReq', 0x2304: 'RealDataRes',
    0x2205: 'CommandReq', 0x2305: 'CommandRes',
    0x2206: 'CommandStatusReq', 0x2306: 'CommandStatusRes',
    0x2207: 'DevConfigFetchReq', 0x2307: 'DevConfigFetchRes',
    0x2208: 'DevConfigPutReq', 0x2308: 'DevConfigPutRes',
    0x220A: 'WaveReq', 0x230A: 'WaveRes',
    0x220B: 'WarnReq', 0x230B: 'WarnRes',
    0x220C: 'RealDataNewReq', 0x230C: 'RealDataNewRes',
    0x220D: 'RealDataNewReq', 0x230D: 'RealDataNewRes',

    0xA201: 'APPInfoDataReq', 0xA301: 'APPInfoDataRes',
    0xA202: 'HBReq', 0xA302: 'HBRes',
    0xA203: 'RealDataReq', 0xA303: 'RealDataRes',
    0xA204: 'WarnReq', 0xA304: 'WarnRes',  # TODO: Also uses AlarmData in one place.
    0xA205: 'CommandReq', 0xA305: 'CommandRes',
    0xA206: 'CommandStatusReq', 0xA306: 'CommandStatusRes',
    0xA207: 'DevConfigFetchReq', 0xA307: 'DevConfigFetchRes',
    0xA208: 'DevConfigPutReq', 0xA308: 'DevConfigPutRes',
    0xA209: 'GetConfigReq', 0xA309: 'GetConfigRes',
    0xA210: 'SetConfigReq', 0xA310: 'SetConfigRes',
    0xA211: 'RealDataNewReq', 0xA311: 'RealDataNewRes',
    0xA212: 'GPSTReq', 0xA312: 'GPSTRes',
    0xA213: 'AutoSearchReq', 0xA313: 'AutoSearchRes',
    0xA214: 'NetworkInfoReq', 0xA314: 'NetworkInfoRes',
    0xA215: 'AppGetHistPowerReq', 0xA315: 'AppGetHistPowerRes',
    0xA216: 'AppGetHistEDReq', 0xA316: 'AppGetHistEDRes',
}

DTU_INTERNAL_IP = '10.10.100.254' # IP of the DTU on the the internal network for the AP (e.g. DTUBI-SerialNumber)
CLOUD_IP = '8.211.32.133'         # IP of the cloud server
DTU_LOCAL_IP = '192.168.XX.XX'    # IP of the DTU on the local (Home / IoT) Network
DUMP_FILE_PATH = 'dumped_messages'# Path to store the dumped messages

# How to use:
# execute the script with the pcapng or tcpdump file as argument e.g.:
# pcap_parser.py capture.pcapng

# Verify that all messages exist.
db = symbol_database.Default()
for command_name in commands.values():
    db.GetSymbol(command_name + 'DTO')

crc16_modbus = crcmod.predefined.Crc('modbus')

counter = 0
for pkt in PcapNgReader(sys.argv[1]):
    if not pkt.haslayer(Raw) or not pkt.haslayer(TCP):
        continue

    timestamp = datetime.fromtimestamp(float(pkt.time)).strftime('%Y-%m-%d %H:%M:%S.%f')
    ip = pkt[IP]
    if ip.src == DTU_INTERNAL_IP:
        direction = 'DTU -> APP'
        color = '\033[0;35m' # Magenta
    elif ip.dst == DTU_INTERNAL_IP:
        direction = 'APP -> DTU'
        color = '\033[0;36m' # Cyam
    elif ip.src == CLOUD_IP:
        direction = 'CLOUD -> DTU'
        color = '\033[0;36m' # Cyam
    elif ip.dst == CLOUD_IP:
        direction = 'DTU -> CLOUD'
        color = '\033[0;35m' # Magenta
    elif ip.src == DTU_LOCAL_IP:
        direction = 'DTU -> Local Apllication'
        color = '\033[0;32m' # Green
    elif ip.dst == DTU_LOCAL_IP:
        direction = 'Local Apllication -> DTU'
        color = '\033[0;33m' # Yellow
    else:
        direction = 'Other'
        color = '\033[0;37m' # White
        # colercodes see: https://gist.github.com/vratiu/9780109

    payload = bytes(pkt[Raw])
    hm, command_id, sequence, crc16, packet_length = struct.unpack(">2s H H H H", payload[0:10])
    command_name = commands.get(command_id, '???')
    data = payload[10:]
    crc_check = "pass" if crc16 == crc16_modbus.new(data).crcValue else "fail"

    print(f"{color}{timestamp} | {direction} | command: {command_id:X} ({command_name}) | sequence: {sequence:X} ({sequence}) | CRC16: {crc16:X} ({crc16}; {crc_check}) | packet length: {packet_length:X} ({packet_length}) |", end='')
    if command_name != '???':
        msg = db.GetSymbol(command_name + 'DTO')()
        msg.ParseFromString(data)
        print(json_format.MessageToDict(msg, preserving_proto_field_name=True), end='')
    else:
        if not os.path.exists(DUMP_FILE_PATH):
            os.makedirs(DUMP_FILE_PATH)
        dump_filename = os.path.join(DUMP_FILE_PATH, os.path.splitext(os.path.basename(sys.argv[1]))[0] + '_msg_' + command_id + '_' + str(counter) + '.dump')
        with open(os.path.join(os.path.dirname(sys.argv[0]),dump_filename), 'wb') as msg_file:
            msg_file.write(payload)
        print('see ' + dump_filename, end='')
        counter += 1
    print('\033[0m')
