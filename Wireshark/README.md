# Wireshark plugin
A Wireshark plugin to add decoding for data transmission between Hoymiles DTUs and the app/Hoymiles Cloud/custom application.


### Disclaimer: 
> [!NOTE]
> This plugin is not affiliated with Wireshark or Hoymiles. It is an independent project developed to provide tools for easier analys of trafic with Hoymiles DTUs and devices connected to them. Any trademarks or product names mentioned are the property of their respective owners.


This plugin is based on the Protobuf example from the [Wireshark Protobuf documentation](https://wiki.wireshark.org/Protobuf), where you can also find additional information and further explanations.


## Protocol structure
Hoymiles uses a proprietary implementation of the [Protobuf Protocol](https://protobuf.dev/) with an Header with additional raw Data about the following Data followed by Data encoded and serialized with the Protobuf Protocol. For mor details about the Protocol strukture see [protocol.md](../protocol.md). This approach has the advantage for the possibility for integrity check of the Data. But with the Disadvantage that a custom plugin like this is required.


## Features / To-dos
- [x] Basic decoding of all header fields
- [x] Mapping the command ID to the correct Protobuf message type
- [x] Decoding the Protobuf message with the associated Protobuf message type
- [x] Checking the length of the data based on the length in the header
- [x] Checking the crc16 against the Protobuf Data (not checked if the calculation is implemented correctly)


## Plugin installation

1. Copy the [Plugin](hoymiles_protobuf_dissector.lua) into the [Plugin Folder from Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/ChPluginFolders.html)
2. Copy all [*.proto](protobuf) files into a (sub)folder (I would recommend putting the subfolder in the same location as the plugin)
    - plugin dir
        - protobuf_files (folder)
            - *.proto files
        - hoymiles_protobuf_dissector.lua
3. Add the **folder** with all the *.proto to the Protobuf search Path
    - `Edit` &rarr; `Preferences` &rarr; `Protocols` &rarr; `ProtoBuf` &rarr; `Protobuf search paths`
4. Check correct Loading of the plugin
    - `Help` &rarr; `About Wireshark` &rarr; `Plugins`

Now you should see in protocol column `TCP_HOYMILES` instead of `TCP` in packets that contain Data.

> [!TIP]
> I would recommend to enable the following settings:
> - Display JSON mapping for Protobuf message
> - Show details of message, fields and enums

> [!TIP]
> If you want to filter only for packets with Data you can use the filter `_ws.col.protocol == "TCP_HOYMILES"`


## Troubleshooting

If it not appears in the list plugin list try reloding of Plugins:
- `Analyze` &rarr; `Reload Lua Plugins (Ctrl-Shift-L)`
- Restart Wireshark


If the automatic adding of the decoder didn't work try adding it manually.
- `Right click a Packet` &rarr; `Decode As...` &rarr; `Add an Entry with the following parameters`:

| Field | Value | Type | Default | Current |
| --- | --- | --- | --- | --- |
| TCP port | 10081 | Integer, base 10 | (none) | TCP_HOYMILES |