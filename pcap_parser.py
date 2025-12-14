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

from protobuf import (AppAUGetHistED_pb2,AppAUGetHistPower_pb2,AppFWOTA_pb2,APPGetConfig_pb2,AppGetHistED_pb2,AppGetHistPower_pb2,APPHeartbeatPB_pb2,APPInfomationData_pb2,APPNetworkInfo_pb2,APPSetConfig_pb2,AUDspCmdSet_pb2,AUInfo_pb2,AURealData_pb2,AutoSearch_pb2,CmdSMLPE_pb2,CommandPB_pb2,CommCmd_pb2,CommDevCfg_pb2,DevConfig_pb2,DevConfigSMLPE_pb2,ESDataPB_pb2,GetConfig_pb2,GPSTData_pb2,GWGetConfig_pb2,GWHeartbeat_pb2,GWInfo_pb2,GWMemRW_pb2,GWNetInfo_pb2,GWSetConfig_pb2,HeartbeatSMLPE_pb2,HPCS_Information_pb2,NetworkInfo_pb2,PV_Inv_Curve_pb2,PV_Inv_Information_pb2,PV_Inv_RT_Data_pb2,RealData_pb2,RealDataNew_pb2,SetConfig_pb2,SMLPEInfo_pb2,SMLPERTData_pb2,SMLPEState_pb2,WarnData_pb2,)

commands = {
    0x2201: 'APPInfoDataReqDTO', 0x2301: 'APPInfoDataResDTO',
    0x2202: 'HBReqDTO', 0x2302: 'HBResDTO',
    0x2203: 'RealDataReqDTO', 0x2303: 'RealDataResDTO',
    0x2204: 'RealDataReqDTO', 0x2304: 'RealDataResDTO',
    0x2205: 'CommandReqDTO', 0x2305: 'CommandResDTO',
    0x2206: 'CommandStatusReqDTO', 0x2306: 'CommandStatusResDTO',
    0x2207: 'DevConfigFetchReqDTO', 0x2307: 'DevConfigFetchResDTO',
    0x2208: 'DevConfigPutReqDTO', 0x2308: 'DevConfigPutResDTO',
    0x220A: 'WaveReqDTO', 0x230A: 'WaveResDTO',
    0x220B: 'WarnReqDTO', 0x230B: 'WarnResDTO',
    0x220C: 'RealReqDTO', 0x230C: 'RealResDTO',
    0x220D: 'RealReqDTO', 0x230D: 'RealResDTO',

    0x3001: 'HbSmlpeReqDTO', 0x3101: 'HbSmlpeResDTO',
    0x8202: 'APPInfoDataReqDTO', 0x8302: 'APPInfoDataResDTO',
    0x8801: 'AUInfoReqDTO', 0x8901: 'AUInfoResDTO',
    0x8802: 'GWHBReqDTO', 0x8902: 'GWHBResDTO',
    0x8803: 'AuRealReqDTO', 0x8903: 'AuRealResDTO',
    # 0x8804: 'AUWarnReqDTO', 0x8904: 'AUWarnResDTO',
    0x8805: 'CommCmdReqDTO', 0x8905: 'CommCmdResDTO',
    0x8806: 'CommCmdStatusReqDTO', 0x8906: 'CommCmdStatusResDTO',
    0x8809: 'APPGetConfigReq', 0x8909: 'APPGetConfigRes',
    0x880A: 'APPSetConfigReq', 0x890A: 'APPSetConfigRes',
    0x880B: 'APPNetworkInfoReq', 0x890B: 'APPNetworkInfoRes',
    0x880C: 'AUGetHistPowerReq', 0x890C: 'AUGetHistPowerRes',
    0x880D: 'AUGetHistEDReq', 0x890D: 'AUGetHistEDRes',
    0x880E: 'FWInfoReqDTO', 0x890E: 'FWInfoResDTO',
    0x880F: 'FWOTAReqDTO', 0x890F: 'FWOTAResDTO',
    0x8810: 'AUDspCmdSetReqDTO', 0x8910: 'AUDspCmdSetResDTO',
    0x8811: 'AUDspCmdGetReqDTO', 0x8911: 'AUDspCmdGetResDTO',
    0xA201: 'APPInfoDataReqDTO', 0xA301: 'APPInfoDataResDTO',
    0xA202: 'HBReqDTO', 0xA302: 'HBResDTO',
    0xA203: 'RealDataReqDTO', 0xA303: 'RealDataResDTO',
    0xA204: 'WarnReqDTO', 0xA304: 'WarnResDTO',
    0xA205: 'CommandReqDTO', 0xA305: 'CommandResDTO',
    0xA206: 'CommandStatusReqDTO', 0xA306: 'CommandStatusResDTO',
    0xA209: 'GetConfigReq', 0xA309: 'GetConfigRes',
    0xA210: 'SetConfigReq', 0xA310: 'SetConfigRes',
    0xA211: 'RealReqDTO', 0xA311: 'RealResDTO',
    0xA212: 'GPSTReqDTO', 0xA312: 'GPSTResDTO',
    0xA213: 'AutoSearchReq', 0xA313: 'AutoSearchRes',
    0xA214: 'NetworkInfoReq', 0xA314: 'NetworkInfoRes',
    0xA215: 'AppGetHistPowerReq', 0xA315: 'AppGetHistPowerRes',
    0xA216: 'AppGetHistEDReq', 0xA316: 'AppGetHistEDRes',
    0xA218: 'CommCmdReqDTO', 0xA318: 'CommCmdResDTO',
    # 0xA218: 'CommCmdStatusReqDTO', 0xA318: 'CommCmdStatusResDTO',
    0xDA01: 'GWInfoReqDTO', 0xDB01: 'GWInfoResDTO',
    # 0xDA01: 'ReadHRegReqDTO', 0xDB01: 'ReadHRegResDTO',
    # 0xDA01: 'CmdSmlpeReqDTO', 0xDB01: 'CmdSmlpeResDTO',
    # 0xDA01: 'ESDataReqDTO', 0xDB01: 'ESDataResDTO',
    # 0xDA01: 'CommCmdReqDTO', 0xDB01: 'CommCmdResDTO',
    # 0xDA01: 'CommCmdStatusReqDTO', 0xDB01: 'CommCmdStatusResDTO',
    # 0xDA01: 'PVInvDataReqDTO', 0xDB01: 'PVInvDataResDTO',
    # 0xDA01: 'PVInvCurveReqDTO', 0xDB01: 'PVInvCurveResDTO',
    # 0xDA01: 'PVInvInfoReqDTO', 0xDB01: 'PVInvInfoResDTO',
    # 0xDA01: 'HPCSInfoReqDTO', 0xDB01: 'HPCSInfoResDTO',
    0xDA02: 'GWHBReqDTO', 0xDB02: 'GWHBResDTO',
    0xDA03: 'CommCmdReqDTO', 0xDB03: 'CommCmdResDTO',
    0xDA04: 'CommCmdStatusReqDTO', 0xDB04: 'CommCmdStatusResDTO',
    0xDA06: 'GWNetInfoReq', 0xDB06: 'GWNetInfoRes',
    0xDA07: 'SetConfigReq', 0xDB07: 'SetConfigRes',
    # 0xDA07: 'GWSetConfigReq', 0xDB07: 'GWSetConfigRes',
    0xDA08: 'GetConfigReq', 0xDB08: 'GetConfigRes',
    # 0xDA08: 'GWGetConfigReq', 0xDB08: 'GWGetConfigRes',
    0xDAFB: 'MemReadReqDTO', 0xDBFB: 'MemReadResDTO',
    # 0xDAFC: 'DTLStateReqDTO', 0xDBFC: 'DTLStateResDTO',
    # 0xDAFC: 'DTLReqDTO', 0xDBFC: 'DTLResDTO',
    0xDAFC: 'MemWriteReqDTO', 0xDBFC: 'MemWriteResDTO',
    # 0xDAFC: 'WriteHRegReqDTO', 0xDBFC: 'WriteHRegResDTO',
    # 0xDAFC: 'InfoReqDTO', 0xDBFC: 'InfoResDTO',
    # 0xDAFC: 'GWSetConfigReq', 0xDBFC: 'GWSetConfigRes',
    # 0xDAFE: 'GWGetConfigReq', 0xDBFE: 'GWGetConfigRes',
    0xDAFE: 'CommDevCfgFetchReqDTO', 0xDBFE: 'CommDevCfgFetchResDTO',
    0xDAFF: 'CommDevCfgPutReqDTO', 0xDBFF: 'CommDevCfgPutResDTO',
    # 0xDAFF: 'GWSetConfigReq', 0xDBFF: 'GWSetConfigRes',
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
    db.GetSymbol(command_name)

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
        msg = db.GetSymbol(command_name)()
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
