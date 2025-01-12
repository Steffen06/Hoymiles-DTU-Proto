# Hoymiles DTU Proto

I created this fork of the original repo because I wanted to add and change some things, but [the original creator of this project does not actively maintain this repo](https://github.com/henkwiedig/Hoymiles-DTU-Proto/pull/2#issuecomment-2438218730).

This Repo contains:
- [Hoymiles DTU protobuf message definitions](protobuf)
- [protocol details](protocol.md)
- a [Wireshark plugin](Wireshark) to add decoding for data transmission between Hoymiles DTUs and the app/Hoymiles Cloud/custom application
- a [pcap file parser](pcap_parser.py) which can parse captured data transmission from *.pcapng files
- a [message parser](message_parser.py) which can parse raw messages extracted from tcpdumps
- some (old) [PoC python scripts](PoC)

You will need python-protobuf and protobuf libs.

Compile *.proto files with protoc. see: [protocol details](protocol.md)

> [!TIP]
> If you want a Python library with more features, see [hoymiles-wifi](https://github.com/suaveolent/hoymiles-wifi)


## Disclaimer: 
> [!NOTE]
> This project is not affiliated with Hoymiles. It is an independent project developed to provide tools for easier analys of trafic with Hoymiles DTUs and devices connected to them. Any trademarks or product names mentioned are the property of their respective owners.


## Bugs, Issues & Questions:

If you find any bugs, errors or something else, feel free to create an Issue, make a Pull request or start a Discussion. I will try to help you as best I can but I collected my knowledge only thru other Projects (see below) and other public Protocol Documentation.


## Attribution:

A special thank you for the inspiration and other Information sources:

- [suaveolent](https://github.com/suaveolent): [hoymiles-wifi](https://github.com/suaveolent/hoymiles-wifi) & [ha-hoymiles-wifi](ha-hoymiles-wifi) (direct communication with DTUs)
- [DennisOSRM](https://github.com/DennisOSRM): [hms-mqtt-publisher](https://github.com/DennisOSRM/hms-mqtt-publisher) (direct communication with DTUs)
- [tbnobody](https://github.com/tbnobody): [OpenDTU](https://github.com/tbnobody/OpenDTU) (open source DTU replacement)