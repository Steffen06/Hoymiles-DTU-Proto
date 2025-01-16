#!/usr/bin/env python3
import sys
import os
from scapy.utils import PcapNgReader
from scapy.layers.inet import IP, TCP
from scapy.packet import Raw
from datetime import datetime
from google.protobuf import symbol_database
from google.protobuf import json_format

import AppGetHistED_pb2
import AppGetHistPower_pb2
import APPHeartbeatPB_pb2
import APPInfomationData_pb2
import AutoSearch_pb2
import CommandPB_pb2
import DevConfig_pb2
import GetConfig_pb2
import GPSTData_pb2
import InfomationData_pb2
import NetworkInfo_pb2
import RealData_pb2
import RealDataNew_pb2
import SetConfig_pb2
import WarnData_pb2

commands = {
    '2201': 'InfoDataReq', '2301': 'InfoDataRes',
    '2202': 'HBReq', '2302': 'HBRes',
    '2203': 'RealDataReq', '2303': 'RealDataRes',
    '2204': 'RealDataReq', '2304': 'RealDataRes',
    '2205': 'CommandReq', '2305': 'CommandRes',
    '2206': 'CommandStatusReq', '2306': 'CommandStatusRes',
    '2207': 'DevConfigFetchReq', '2307': 'DevConfigFetchRes',
    '2208': 'DevConfigPutReq', '2308': 'DevConfigPutRes',
    '220A': 'WaveReq', '230A': 'WaveRes',
    '220B': 'WarnReq', '230B': 'WarnRes',
    '220C': 'RealDataNewReq', '230C': 'RealDataNewRes',
    '220D': 'RealDataNewReq', '230D': 'RealDataNewRes',

    'A201': 'APPInfoDataReq', 'A301': 'APPInfoDataRes',
    'A202': 'HBReq', 'A302': 'HBRes',
    'A203': 'RealDataReq', 'A303': 'RealDataRes',
    'A204': 'WarnReq', 'A304': 'WarnRes',  # TODO: Also uses AlarmData in one place.
    'A205': 'CommandReq', 'A305': 'CommandRes',
    'A206': 'CommandStatusReq', 'A306': 'CommandStatusRes',
    'A207': 'DevConfigFetchReq', 'A307': 'DevConfigFetchRes',
    'A208': 'DevConfigPutReq', 'A308': 'DevConfigPutRes',
    'A209': 'GetConfigReq', 'A309': 'GetConfigRes',
    'A210': 'SetConfigReq', 'A310': 'SetConfigRes',
    'A211': 'RealDataNewReq', 'A311': 'RealDataNewRes',
    'A212': 'GPSTReq', 'A312': 'GPSTRes',
    'A213': 'AutoSearchReq', 'A313': 'AutoSearchRes',
    'A214': 'NetworkInfoReq', 'A314': 'NetworkInfoRes',
    'A215': 'AppGetHistPowerReq', 'A315': 'AppGetHistPowerRes',
    'A216': 'AppGetHistEDReq', 'A316': 'AppGetHistEDRes',
}

DTU_INTERNAL_IP = '10.10.100.254' # IP of the DTU on the the internal network for the AP (e.g. DTUBI-SerialNumber)
CLOUD_IP = '8.211.32.133'         # IP of the cloud server
DTU_LOCAL_IP = '192.168.XX.XX'    # IP of the DTU on the local (Home / IoT) Network
DUMP_FILE_PATH = 'dumped_messages'# Path to store the dumped messages

# How to use:
# execute the script with the pcapng file as argument e.g.:
# python.exe pcap_parser.py capture.pcapng

# Verify that all messages exist.
db = symbol_database.Default()
for command_name in commands.values():
    db.GetSymbol(command_name + 'DTO')

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
    command_id = payload[2:4].hex().upper()
    command_name = commands.get(command_id, '???')
    seq = payload[4:6]
    data = payload[10:]
    print('%s%s | %s | command %s (%s) | seq %s | ' % (color, timestamp, direction, command_id, command_name, seq.hex().upper()), end='')
    if command_name == '???':
        if not os.path.exists(DUMP_FILE_PATH):
            os.makedirs(DUMP_FILE_PATH)
        dump_filename = os.path.join(DUMP_FILE_PATH, os.path.splitext(os.path.basename(sys.argv[1]))[0] + '_msg_' + command_id + '_' + str(counter) + '.dump')
        with open(os.path.join(os.path.dirname(sys.argv[0]),dump_filename), 'wb') as msg_file:
            msg_file.write(payload)
        print('see ' + dump_filename, end='')
        counter += 1
    else:
        msg = db.GetSymbol(command_name + 'DTO')()
        msg.ParseFromString(data)
        print(json_format.MessageToDict(msg, preserving_proto_field_name=True), end='')
    print('\033[0m')
