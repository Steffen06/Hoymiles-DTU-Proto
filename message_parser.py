#!/usr/bin/env python3
import struct
import AppGetHistPower_pb2
import APPInfomationData_pb2
import APPHeartbeatPB_pb2
import AppGetHistED_pb2
import CommandPB_pb2
import NetworkInfo_pb2
import GetConfig_pb2
import SetConfig_pb2
import RealData_pb2
import AlarmData_pb2
import sys
import crcmod.predefined
from google.protobuf import symbol_database
from google.protobuf import json_format

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

# Verify that all messages exist.
db = symbol_database.Default()
for command_name in commands.values():
    db.GetSymbol(command_name + 'DTO')

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
            msg = db.GetSymbol(command_name + 'DTO')()
            msg.ParseFromString(data)
            print(json_format.MessageToDict(msg, preserving_proto_field_name=True))
        # else:
            #print(f"Header: {header_data}")
            #print(f"Payload: {data}")

# Close the file when done
file.close()
