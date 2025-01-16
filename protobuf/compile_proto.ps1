# compile all .proto files in the current directory
# requires protoc.exe in the PATH
# download from https://github.com/protocolbuffers/protobuf/releases

foreach ($file in Get-ChildItem -Filter *.proto) {
    protoc.exe --python_out=. $file
}