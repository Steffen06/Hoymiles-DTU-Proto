# Hoymiles DTU Proto

I created this fork of the original repo because I wanted to add and change some things, but [the original creator of this project does not actively maintain this repo](https://github.com/henkwiedig/Hoymiles-DTU-Proto/pull/2#issuecomment-2438218730).

This Repo contains Hoymiles DTU protobuf message definitions and protocol details.

Some POC python scripts and a message parser wich can parse raw messages extracted from tcpdumps.

You will need python-protobuf and protobuf libs.

> [!TIP]
> If you want a Python library with more features, see [hoymiles-wifi](https://github.com/suaveolent/hoymiles-wifi)

Compile *.proto files with protoc. see: [protocol.md](protocol.md)


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