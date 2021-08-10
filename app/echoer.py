from app.generated.echo_pb2_grpc import EchoServicer
from app.generated.echo_pb2 import EchoReply

class Echoer(EchoServicer):

    def Reply(self, request, context):
        return EchoReply(message=f'You said: {request.message}')



