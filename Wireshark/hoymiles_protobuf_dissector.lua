do
    local command_id_map = {
        [0x2201] = "InfoDataReqDTO", [0x2301] = "InfoDataResDTO",
        [0x2202] = "HBReqDTO", [0x2302] = "HBResDTO",
        [0x2203] = "RealDataReqDTO", [0x2303] = "RealDataResDTO",
        [0x2204] = "RealDataReqDTO", [0x2304] = "RealDataResDTO",
        [0x2205] = "CommandReqDTO", [0x2305] = "CommandResDTO",
        [0x2206] = "CommandStatusReqDTO", [0x2306] = "CommandStatusResDTO",
        [0x2207] = "DevConfigFetchReqDTO", [0x2307] = "DevConfigFetchResDTO",
        [0x2208] = "DevConfigPutReqDTO", [0x2308] = "DevConfigPutResDTO",
        [0x220A] = "WaveReqDTO", [0x230A] = "WaveResDTO",
        [0x220B] = "WarnReqDTO", [0x230B] = "WarnResDTO",
        [0x220C] = "RealDataNewReqDTO", [0x230C] = "RealDataNewResDTO",
        [0x220D] = "RealDataNewReqDTO", [0x230D] = "RealDataNewResDTO",

        [0xA201] = "APPInfoDataReqDTO", [0xA301] = "APPInfoDataResDTO",
        [0xA202] = "HBReqDTO", [0xA302] = "HBResDTO",
        [0xA203] = "RealDataReqDTO", [0xA303] = "RealDataResDTO",
        [0xA204] = "WarnReqDTO", [0xA304] = "WarnResDTO",
        [0xA205] = "CommandReqDTO", [0xA305] = "CommandResDTO",
        [0xA206] = "CommandStatusReqDTO", [0xA306] = "CommandStatusResDTO",
        [0xA207] = "DevConfigFetchReqDTO", [0xA307] = "DevConfigFetchResDTO",
        [0xA208] = "DevConfigPutReqDTO", [0xA308] = "DevConfigPutResDTO",
        [0xA209] = "GetConfigReqDTO", [0xA309] = "GetConfigResDTO",
        [0xA210] = "SetConfigReqDTO", [0xA310] = "SetConfigResDTO",
        [0xA211] = "RealDataNewReqDTO", [0xA311] = "RealDataNewResDTO",
        [0xA212] = "GPSTReqDTO", [0xA312] = "GPSTResDTO",
        [0xA213] = "AutoSearchReqDTO", [0xA313] = "AutoSearchResDTO",
        [0xA214] = "NetworkInfoReqDTO", [0xA314] = "NetworkInfoResDTO",
        [0xA215] = "AppGetHistPowerReqDTO", [0xA315] = "AppGetHistPowerResDTO",
        [0xA216] = "AppGetHistEDReqDTO", [0xA316] = "AppGetHistEDResDTO",
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