#!/bin/bash
# compile all .proto files in the current directory

for file in $(ls *.proto)
do
  protoc --python_out=. $file
done