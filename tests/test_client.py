
from context import app
import grpc

def test_reply(grpc_stub):
    value = 'test-data-2'
    request = app.echo_pb2.EchoRequest(message=value)
    response = grpc_stub.Reply(request)

    print(response.message)
    assert response.message == f'You said: {value}'

channel = grpc.insecure_channel('localhost:50051', options=(('grpc.enable_http_proxy', 0),))

grpc_stub = app.generated.echo_pb2_grpc.EchoStub(channel)
test_reply(grpc_stub)