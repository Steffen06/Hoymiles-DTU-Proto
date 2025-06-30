do
    local command_id_map = {
        [0x2201] = "APPInfoDataReqDTO", [0x2301] = "APPInfoDataResDTO",
        [0x2202] = "HBReqDTO", [0x2302] = "HBResDTO",
        [0x2203] = "RealDataReqDTO", [0x2303] = "RealDataResDTO",
        [0x2204] = "RealDataReqDTO", [0x2304] = "RealDataResDTO",
        [0x2205] = "CommandReqDTO", [0x2305] = "CommandResDTO",
        [0x2206] = "CommandStatusReqDTO", [0x2306] = "CommandStatusResDTO",
        [0x2207] = "DevConfigFetchReqDTO", [0x2307] = "DevConfigFetchResDTO",
        [0x2208] = "DevConfigPutReqDTO", [0x2308] = "DevConfigPutResDTO",
        [0x220A] = "WaveReqDTO", [0x230A] = "WaveResDTO",
        [0x220B] = "WarnReqDTO", [0x230B] = "WarnResDTO",
        [0x220C] = "RealReqDTO", [0x230C] = "RealResDTO",
        [0x220D] = "RealReqDTO", [0x230D] = "RealResDTO",

        [0x3001] = "HbSmlpeReqDTO", [0x3101] = "HbSmlpeResDTO",
        [0x3002] = "ReadHRegReqDTO", [0x3102] = "ReadHRegResDTO",
        [0x3003] = "WriteHRegReqDTO", [0x3103] = "WriteHRegResDTO",
        [0x3008] = "CmdSmlpeReqDTO", [0x3108] = "CmdSmlpeResDTO",
        [0x8201] = "HBReqDTO", [0x8301] = "HBResDTO",
        -- [0x8202] = "StorageRegisterReqDTO", [0x8302] = "RegisterResDTO",
        -- [0x8203] = "StorageDataReqDTO", [0x8303] = "StorageDataRes",
        [0x8205] = "CommandReqDTO", [0x8305] = "CommandResDTO",
        [0x8206] = "CommandStatusReqDTO", [0x8306] = "CommandStatusResDTO",
        [0x8207] = "DevConfigFetchReqDTO", [0x8307] = "DevConfigFetchResDTO",
        [0x8208] = "DevConfigPutReqDTO", [0x8308] = "DevConfigPutResDTO",
        [0x8801] = "AUInfoReqDTO", [0x8901] = "AUInfoResDTO",
        [0x8802] = "GWHBReqDTO", [0x8902] = "GWHBResDTO",
        [0x8803] = "AuRealReqDTO", [0x8903] = "AuRealResDTO",
        -- [0x8804] = "AUWarnReqDTO", [0x8904] = "AUWarnResDTO",
        [0x8805] = "CommCmdReqDTO", [0x8905] = "CommCmdResDTO",
        [0x8806] = "CommCmdStatusReqDTO", [0x8906] = "CommCmdStatusResDTO",
        [0x8809] = "APPGetConfigReq", [0x8909] = "APPGetConfigRes",
        [0x880A] = "APPSetConfigReq", [0x890A] = "APPSetConfigRes",
        [0x880B] = "APPNetworkInfoReq", [0x890B] = "APPNetworkInfoRes",
        [0x880C] = "AUGetHistPowerReq", [0x890C] = "AUGetHistPowerRes",
        [0x880D] = "AUGetHistEDReq", [0x890D] = "AUGetHistEDRes",
        [0x880E] = "FWInfoReqDTO", [0x890E] = "FWInfoResDTO",
        [0x880F] = "FWOTAReqDTO", [0x890F] = "FWOTAResDTO",
        [0x8810] = "AUDspCmdSetReqDTO", [0x8910] = "AUDspCmdSetResDTO",
        [0x8811] = "AUDspCmdGetReqDTO", [0x8911] = "AUDspCmdGetResDTO",
        [0xA201] = "APPInfoDataReqDTO", [0xA301] = "APPInfoDataResDTO",
        [0xA202] = "HBReqDTO", [0xA302] = "HBResDTO",
        [0xA203] = "RealDataReqDTO", [0xA303] = "RealDataResDTO",
        [0xA204] = "WarnReqDTO", [0xA304] = "WarnResDTO",
        -- [0xA204] = "WInfoReqDTO", [0xA304] = "WInfoResDTO",
        [0xA205] = "CommandReqDTO", [0xA305] = "CommandResDTO",
        [0xA206] = "CommandStatusReqDTO", [0xA306] = "CommandStatusResDTO",
        [0xA207] = "DevConfigFetchReqDTO", [0xA307] = "DevConfigFetchResDTO",
        [0xA208] = "DevConfigPutReqDTO", [0xA308] = "DevConfigPutResDTO",
        [0xA209] = "GetConfigReq", [0xA309] = "GetConfigRes",
        [0xA210] = "SetConfigReq", [0xA310] = "SetConfigRes",
        [0xA211] = "RealReqDTO", [0xA311] = "RealResDTO",
        -- [0xA211] = "APPInfoDataReqDTO", [0xA311] = "APPInfoDataResDTO",
        [0xA212] = "GPSTReqDTO", [0xA312] = "GPSTResDTO",
        [0xA213] = "AutoSearchReq", [0xA313] = "AutoSearchRes",
        [0xA214] = "NetworkInfoReq", [0xA314] = "NetworkInfoRes",
        -- [0xA214] = "GetConfigReq", [0xA314] = "GetConfigRes",
        -- [0xA214] = "SetConfigReq", [0xA314] = "SetConfigRes",
        [0xA215] = "AppGetHistPowerReq", [0xA315] = "AppGetHistPowerRes",
        [0xA216] = "AppGetHistEDReq", [0xA316] = "AppGetHistEDRes",
        [0xC202] = "ESRegReqDTO", [0xC302] = "ESRegResDTO",
        [0xC203] = "ESDataReqDTO", [0xC303] = "ESDataResDTO",
        [0xC207] = "ESUserSetPutResDTO", [0xC307] = "ESUserSetPutReqDTO",
        [0xC208] = "ESUserSetPutReqDTO", [0xC308] = "ESUserSetPutResDTO",
        [0xC2FE] = "CommDevCfgFetchReqDTO", [0xC3FE] = "CommDevCfgFetchResDTO",
        [0xC2FF] = "CommDevCfgPutReqDTO", [0xC3FF] = "CommDevCfgPutResDTO",
        [0xC802] = "PVInvInfoReqDTO", [0xC902] = "PVInvInfoResDTO",
        [0xC803] = "PVInvDataReqDTO", [0xC903] = "PVInvDataResDTO",
        [0xC807] = "PVInvUserSetGetReqDTO", [0xC907] = "PVInvUserSetGetResDTO",
        [0xC808] = "PVInvUserSetGetResDTO", [0xC908] = "PVInvUserSetGetReqDTO",
        [0xC809] = "PVInvWarnReqDTO", [0xC909] = "PVInvWarnResDTO",
        [0xC843] = "PVInvUpdateReqDTO", [0xC943] = "PVInvUpdateResDTO",
        [0xC844] = "PVInvOTAReqDTO", [0xC944] = "PVInvOTAResDTO",
        [0xC8C0] = "PVInvCurveReqDTO", [0xC9C0] = "PVInvCurveResDTO",
        [0xC8C1] = "PVInvEnergyCurveReqDTO", [0xC9C1] = "PVInvEnergyCurveResDTO",
        [0xC8D0] = "PVInvEventLogReqDTO", [0xC9D0] = "PVInvEventLogResDTO",
        [0xCC02] = "HPCSInfoReqDTO", [0xCD02] = "HPCSInfoResDTO",
        [0xCC03] = "HPCSDataReqDTO", [0xCD03] = "HPCSDataResDTO",
        -- [0xCC03] = "HPCSLRDataReqDTO", [0xCD03] = "HPCSLRDataResDTO",
        -- [0xCC03] = "HPCSInfoReqDTO", [0xCD03] = "HPCSInfoResDTO",
        -- [0xCC07] = "HPCSLRUserSetGetReqDTO", [0xCD07] = "HPCSLRUserSetGetResDTO",
        [0xCC07] = "HPCSUserSetGetReqDTO", [0xCD07] = "HPCSUserSetGetResDTO",
        -- [0xCC08] = "HPCSLRUserSetGetResDTO", [0xCD08] = "HPCSLRUserSetGetReqDTO",
        [0xCC08] = "HPCSUserSetGetResDTO", [0xCD08] = "HPCSUserSetGetReqDTO",
        [0xCC09] = "HPCSWarnReqDTO", [0xCD09] = "HPCSWarnResDTO",
        [0xDA01] = "GWInfoReqDTO", [0xDB01] = "GWInfoResDTO",
        -- [0xDA01] = "GWGetConfigReq", [0xDB01] = "GWGetConfigRes",
        -- [0xDA01] = "GWSetConfigReq", [0xDB01] = "GWSetConfigRes",
        [0xDA02] = "GWHBReqDTO", [0xDB02] = "GWHBResDTO",
        [0xDA03] = "CommCmdReqDTO", [0xDB03] = "CommCmdResDTO",
        [0xDA04] = "CommCmdStatusReqDTO", [0xDB04] = "CommCmdStatusResDTO",
        [0xDA06] = "GWNetInfoReq", [0xDB06] = "GWNetInfoRes",
        -- [0xDA06] = "GWGetConfigReq", [0xDB06] = "GWGetConfigRes",
        -- [0xDA06] = "GWSetConfigReq", [0xDB06] = "GWSetConfigRes",
        [0xDA07] = "SetConfigReq", [0xDB07] = "SetConfigRes",
        [0xDA08] = "GetConfigReq", [0xDB08] = "GetConfigRes",
        [0xDAFB] = "MemReadReqDTO", [0xDBFB] = "MemReadResDTO",
        [0xDAFC] = "MemWriteReqDTO", [0xDBFC] = "MemWriteResDTO",
        [0xDAFE] = "CommDevCfgFetchReqDTO", [0xDBFE] = "CommDevCfgFetchResDTO",
        [0xDAFF] = "CommDevCfgPutReqDTO", [0xDBFF] = "CommDevCfgPutResDTO",
        [0xF002] = "InfoReqDTO", [0xF102] = "InfoResDTO",
        [0xF003] = "DTLReqDTO", [0xF103] = "DTLResDTO",
        [0xF004] = "DTLStateReqDTO", [0xF104] = "DTLStateResDTO",
        [0xF005] = "SMLPENetworkReqDTO", [0xF105] = "SMLPENetworkResDTO",
    }
    
    
    local protobuf_dissector = Dissector.get("protobuf")

    -- Hoymiles protobuf protocol dissector
    -- This dissector is based on the protobuf dissector
    -- 2 Bytes Header HM (0x484D) as string
    -- 2 Bytes Comand ID 
    -- 2 Bytes Sequence ID
    -- 2 Bytes Crc16 Checksum
    -- 2 Bytes Length
    -- n Bytes protobuf message

    local proto_hoymiles = Proto("TCP_Hoymiles", "Hoymiles Protobuf Protocol")
    local f_header = ProtoField.string("hoymiles.header", "Header")
    local f_command_id = ProtoField.uint16("hoymiles.command_id", "Command ID", base.HEX)
    local f_sequence_id = ProtoField.uint16("hoymiles.sequence_id", "Sequence ID", base.HEX)
    local f_crc16 = ProtoField.uint16("hoymiles.crc16", "CRC16", base.HEX)
    local f_length = ProtoField.uint16("hoymiles.length", "Length", base.DEC)

    proto_hoymiles.fields = {f_header, f_command_id, f_sequence_id, f_crc16, f_length}
    
    function proto_hoymiles.dissector(buffer, pinfo, tree)
        pinfo.cols.protocol = proto_hoymiles.name

        local subtree = tree:add(proto_hoymiles, buffer(), "Hoymiles Protocol Data")
        local header = buffer(0, 2)
        local command_id = buffer(2, 2)
        local command_name = command_id_map[command_id:uint()]
        local sequence_id = buffer(4, 2)
        local crc16 = buffer(6, 2)
        local length = buffer(8, 2)
        local payload = buffer(10):tvb()
        local crc16_modbus = crc(payload, 0xA001, 0xFFFF, 0)
        subtree:add(f_header, header)
        subtree:add(f_command_id, command_id):append_text(" (" .. (command_name or "Unknown") .. ")")
        subtree:add(f_sequence_id, sequence_id)
        if crc16_modbus == crc16:uint() then
            subtree:add(f_crc16, crc16):append_text(" (CRC16 OK)")
        else
            subtree:add(f_crc16, crc16):append_text(" (CRC16 ERROR)")
        end
        if length:uint() - 10 == payload:len() then
            subtree:add(f_length, length):append_text(" (Length OK)")
        else
            subtree:add(f_length, length):append_text(" (Length ERROR)")
        end
        
        -- Dissect the protobuf message
        if command_name then
            pinfo.private["pb_msg_type"] = "message," .. command_name
        end
        protobuf_dissector:call(payload, pinfo, subtree)
    end

    DissectorTable.get("tcp.port"):add(10081, proto_hoymiles)

    function crc(data, poly, init, xorout)
        local crc = init
        for i = 0, data:len() - 1 do
            crc = bit.bxor(crc, data(i, 1):uint())
            for j = 0, 7 do
                if bit.band(crc, 1) == 1 then
                    crc = bit.bxor(bit.rshift(crc, 1), poly)
                else
                    crc = bit.rshift(crc, 1)
                end
            end
        end
        return bit.bxor(crc, xorout)
    end
end