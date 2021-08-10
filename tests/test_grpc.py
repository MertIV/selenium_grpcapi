from app.generated.echo_pb2 import EchoRequest

def test_reply(grpc_stub):
    value = 'test-data'
    request = EchoRequest(message=value)
    response = grpc_stub.Reply(request)

    assert response.message == f'You said: {value}'
