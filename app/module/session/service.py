from app.generated.session_pb2_grpc import SessionServiceServicer
from app.generated.session_pb2 import Session,SessionRequest,StringResponse,IdRequest

class Session(SessionServiceServicer):

    def Create(self, request, context):
        return super().Create(request, context)

    def Update(self, request, context):
        return super().Update(request, context)

    def Delete(self, request, context):
        return super().Delete(request, context)