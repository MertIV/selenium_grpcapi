import pytest


@pytest.fixture(scope='module')
def grpc_add_to_server():
    from app.generated.echo_pb2_grpc import add_EchoServicer_to_server

    return add_EchoServicer_to_server


@pytest.fixture(scope='module')
def grpc_servicer():
    from app.echoer import Echoer

    return Echoer()


@pytest.fixture(scope='module')
def grpc_stub(grpc_channel):
    from app.generated.echo_pb2_grpc import EchoStub

    return EchoStub(grpc_channel)
