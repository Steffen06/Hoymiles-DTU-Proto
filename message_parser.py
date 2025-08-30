#!/usr/bin/env python3
import struct
import sys
import crcmod.predefined
from google.protobuf import symbol_database
from google.protobuf import json_format

from protobuf import (AlarmData_pb2,AppAUGetHistED_pb2,AppAUGetHistPower_pb2,AppFWOTA_pb2,APPGetConfig_pb2,AppGetHistED_pb2,AppGetHistPower_pb2,APPHeartbeatPB_pb2,APPInfomationData_pb2,APPNetworkInfo_pb2,APPSetConfig_pb2,AUDspCmdSet_pb2,AUInfo_pb2,AURealData_pb2,AutoSearch_pb2,CfgRuleConfigPB_pb2,ChartPB_pb2,CmdSMLPE_pb2,CommandPB_pb2,CommCmd_pb2,CommDevCfg_pb2,DevConfigSMLPE_pb2,DevConfig_pb2,ESCheckPB_pb2,ESCommCfg_pb2,ESCPCfg_pb2,ESDataPB_pb2,ESDebugLog_pb2,ESParaSet_pb2,ESRegPB_pb2,ESUserSet_pb2,EventData_pb2,FileDataSMLPE_pb2,GetConfig_pb2,GPSTData_pb2,GWGetConfig_pb2,GWHeartbeat_pb2,GWInfo_pb2,GWMemRW_pb2,GWNetInfo_pb2,GWSetConfig_pb2,GWWarn_pb2,HeartbeatSMLPE_pb2,HPCSLR_Information_pb2,HPCSLR_RT_Data_pb2,HPCSLR_UserSet_pb2,HPCSLR_Warn_pb2,HPCS_Information_pb2,HPCS_RT_Data_pb2,HPCS_UserSet_pb2,HPCS_Warn_pb2,NetworkInfo_pb2,PlaybackDataPB_pb2,PV_Inv_Curve_pb2,PV_Inv_EnergyCurve_pb2,PV_Inv_EventLog_pb2,PV_Inv_Information_pb2,PV_Inv_RT_Data_pb2,PV_Inv_Update_pb2,PV_Inv_UserSet_pb2,PV_Inv_Warn_pb2,RealDataNew_pb2,RealData_pb2,SetConfig_pb2,SMLPEInfo_pb2,SMLPENetwork_pb2,SMLPERTData_pb2,SMLPEState_pb2,StorageRegisterPB_pb2,WarnData_pb2,)

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
    0x3002: 'ReadHRegReqDTO', 0x3102: 'ReadHRegResDTO',
    0x3003: 'WriteHRegReqDTO', 0x3103: 'WriteHRegResDTO',
    0x3008: 'CmdSmlpeReqDTO', 0x3108: 'CmdSmlpeResDTO',
    0x8201: 'HBReqDTO', 0x8301: 'HBResDTO',
    # 0x8202: 'StorageRegisterReqDTO', 0x8302: 'RegisterResDTO',
    # 0x8203: 'StorageDataReqDTO', 0x8303: 'StorageDataRes',
    0x8205: 'CommandReqDTO', 0x8305: 'CommandResDTO',
    0x8206: 'CommandStatusReqDTO', 0x8306: 'CommandStatusResDTO',
    0x8207: 'DevConfigFetchReqDTO', 0x8307: 'DevConfigFetchResDTO',
    0x8208: 'DevConfigPutReqDTO', 0x8308: 'DevConfigPutResDTO',
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
    # 0xA204: 'WInfoReqDTO', 0xA304: 'WInfoResDTO',
    0xA205: 'CommandReqDTO', 0xA305: 'CommandResDTO',
    0xA206: 'CommandStatusReqDTO', 0xA306: 'CommandStatusResDTO',
    0xA207: 'DevConfigFetchReqDTO', 0xA307: 'DevConfigFetchResDTO',
    0xA208: 'DevConfigPutReqDTO', 0xA308: 'DevConfigPutResDTO',
    0xA209: 'GetConfigReq', 0xA309: 'GetConfigRes',
    0xA210: 'SetConfigReq', 0xA310: 'SetConfigRes',
    0xA211: 'RealReqDTO', 0xA311: 'RealResDTO',
    # 0xA211: 'APPInfoDataReqDTO', 0xA311: 'APPInfoDataResDTO',
    0xA212: 'GPSTReqDTO', 0xA312: 'GPSTResDTO',
    0xA213: 'AutoSearchReq', 0xA313: 'AutoSearchRes',
    0xA214: 'NetworkInfoReq', 0xA314: 'NetworkInfoRes',
    # 0xA214: 'GetConfigReq', 0xA314: 'GetConfigRes',
    # 0xA214: 'SetConfigReq', 0xA314: 'SetConfigRes',
    0xA215: 'AppGetHistPowerReq', 0xA315: 'AppGetHistPowerRes',
    0xA216: 'AppGetHistEDReq', 0xA316: 'AppGetHistEDRes',
    0xC202: 'ESRegReqDTO', 0xC302: 'ESRegResDTO',
    0xC203: 'ESDataReqDTO', 0xC303: 'ESDataResDTO',
    0xC207: 'ESUserSetPutResDTO', 0xC307: 'ESUserSetPutReqDTO',
    0xC208: 'ESUserSetPutReqDTO', 0xC308: 'ESUserSetPutResDTO',
    0xC2FE: 'CommDevCfgFetchReqDTO', 0xC3FE: 'CommDevCfgFetchResDTO',
    0xC2FF: 'CommDevCfgPutReqDTO', 0xC3FF: 'CommDevCfgPutResDTO',
    # 0xC2FF: 'ESHMIDCfgMO', 0xC3FF: 'ESCOMMCfgBO',
    0xC802: 'PVInvInfoReqDTO', 0xC902: 'PVInvInfoResDTO',
    0xC803: 'PVInvDataReqDTO', 0xC903: 'PVInvDataResDTO',
    0xC807: 'PVInvUserSetGetReqDTO', 0xC907: 'PVInvUserSetGetResDTO',
    0xC808: 'PVInvUserSetGetResDTO', 0xC908: 'PVInvUserSetGetReqDTO',
    0xC809: 'PVInvWarnReqDTO', 0xC909: 'PVInvWarnResDTO',
    0xC843: 'PVInvUpdateReqDTO', 0xC943: 'PVInvUpdateResDTO',
    0xC844: 'PVInvOTAReqDTO', 0xC944: 'PVInvOTAResDTO',
    0xC8C0: 'PVInvCurveReqDTO', 0xC9C0: 'PVInvCurveResDTO',
    0xC8C1: 'PVInvEnergyCurveReqDTO', 0xC9C1: 'PVInvEnergyCurveResDTO',
    0xC8D0: 'PVInvEventLogReqDTO', 0xC9D0: 'PVInvEventLogResDTO',
    0xCC02: 'HPCSInfoReqDTO', 0xCD02: 'HPCSInfoResDTO',
    0xCC03: 'HPCSDataReqDTO', 0xCD03: 'HPCSDataResDTO',
    # 0xCC03: 'HPCSLRDataReqDTO', 0xCD03: 'HPCSLRDataResDTO',
    # 0xCC03: 'HPCSInfoReqDTO', 0xCD03: 'HPCSInfoResDTO',
    # 0xCC07: 'HPCSLRUserSetGetReqDTO', 0xCD07: 'HPCSLRUserSetGetResDTO',
    0xCC07: 'HPCSUserSetGetReqDTO', 0xCD07: 'HPCSUserSetGetResDTO',
    # 0xCC08: 'HPCSLRUserSetGetResDTO', 0xCD08: 'HPCSLRUserSetGetReqDTO',
    0xCC08: 'HPCSUserSetGetResDTO', 0xCD08: 'HPCSUserSetGetReqDTO',
    0xCC09: 'HPCSWarnReqDTO', 0xCD09: 'HPCSWarnResDTO',
    0xDA01: 'GWInfoReqDTO', 0xDB01: 'GWInfoResDTO',
    # 0xDA01: 'GWGetConfigReq', 0xDB01: 'GWGetConfigRes',
    # 0xDA01: 'GWSetConfigReq', 0xDB01: 'GWSetConfigRes',
    0xDA02: 'GWHBReqDTO', 0xDB02: 'GWHBResDTO',
    0xDA03: 'CommCmdReqDTO', 0xDB03: 'CommCmdResDTO',
    0xDA04: 'CommCmdStatusReqDTO', 0xDB04: 'CommCmdStatusResDTO',
    0xDA06: 'GWNetInfoReq', 0xDB06: 'GWNetInfoRes',
    # 0xDA06: 'GWGetConfigReq', 0xDB06: 'GWGetConfigRes',
    # 0xDA06: 'GWSetConfigReq', 0xDB06: 'GWSetConfigRes',
    0xDA07: 'SetConfigReq', 0xDB07: 'SetConfigRes',
    0xDA08: 'GetConfigReq', 0xDB08: 'GetConfigRes',
    0xDAFB: 'MemReadReqDTO', 0xDBFB: 'MemReadResDTO',
    0xDAFC: 'MemWriteReqDTO', 0xDBFC: 'MemWriteResDTO',
    0xDAFE: 'CommDevCfgFetchReqDTO', 0xDBFE: 'CommDevCfgFetchResDTO',
    0xDAFF: 'CommDevCfgPutReqDTO', 0xDBFF: 'CommDevCfgPutResDTO',
    0xF002: 'InfoReqDTO', 0xF102: 'InfoResDTO',
    0xF003: 'DTLReqDTO', 0xF103: 'DTLResDTO',
    0xF004: 'DTLStateReqDTO', 0xF104: 'DTLStateResDTO',
    0xF005: 'SMLPENetworkReqDTO', 0xF105: 'SMLPENetworkResDTO',
}

# How to use:
# execute the script with the dump file from pcap_parser.py as argument e.g.:
# message_parser.py dumped_messages\capture.dump

# Verify that all messages exist.
db = symbol_database.Default()
for command_name in commands.values():
    db.GetSymbol(command_name)

crc16_modbus = crcmod.predefined.Crc('modbus')

# Open the binary file for reading
with open(sys.argv[1], "rb") as file:
    while True:
        # Read the 'HM' and header fields
        header_data = file.read(10)  # Adjusted for the 2-byte total length field

        # Break the loop if no more data is left
        if len(header_data) < 10:  # Adjusted for the 2-byte total length field
            break

        hm, command_id, sequence, crc16, packet_length = struct.unpack(">2s H H H H", header_data)
        command_name = commands.get(command_id, '???')

        # Read the data based on the packet_length
        data = file.read(packet_length - 10)  # Subtract 10 for the header size
        crc_check = "pass" if crc16 == crc16_modbus.new(data).crcValue else "fail"

        # Process the packet data as needed
        print(f"HM:{int.from_bytes(hm):X} ({hm.decode('utf-8')})| command: {command_id:X} ({command_name if command_name != '???' else "unknown / unsuppoted"}; {command_id}) | sequence: {sequence:X} ({sequence}) | CRC16: {crc16:X} ({crc16}; {crc_check}) | packet length: {packet_length:X} ({packet_length}) |", end='')
        if command_name != '???':
            msg = db.GetSymbol(command_name)()
            msg.ParseFromString(data)
            print(json_format.MessageToDict(msg, preserving_proto_field_name=True))
        # else:
            #print(f"Header: {header_data}")
            #print(f"Payload: {data}")

# Close the file when done
file.close()
