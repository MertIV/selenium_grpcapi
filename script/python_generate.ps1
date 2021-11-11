python -m grpc_tools.protoc -I app/proto --python_out=./app/generated --grpc_python_out=./app/generated ./app/proto/*.proto
sed -i -E 's/^import.*_pb2/from . \0/' ./app/generated/*.py
