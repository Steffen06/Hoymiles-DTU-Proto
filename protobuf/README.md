# Modefied protobuf files

This folder contains modified protobuf files. For unmodified protobuf files or mapping of command IDs to commands see [src_proto](../src_proto/).

## Modifications

The Following Things may be modified:
- removed optional field modefiers
- changed field Types
   - bytes -> string
- addied comments
- changed varibel names

## compile prot files to python code

To compile for python scripts necessary files you can use [linux script](compile_proto.sh) or [windows script](compile_proto.ps1). This scripts run the folling `protoc -I=protobuf --python_out=. <prtobuf file>` for every protobuf file in the directory.
