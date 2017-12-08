# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import PushData_pb2 as PushData__pb2


class PushServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Login = channel.unary_stream(
        '/PushService/Login',
        request_serializer=PushData__pb2.UserInfo.SerializeToString,
        response_deserializer=PushData__pb2.ResponseInfo.FromString,
        )
    self.SendMessage = channel.unary_unary(
        '/PushService/SendMessage',
        request_serializer=PushData__pb2.SendMessageInfo.SerializeToString,
        response_deserializer=PushData__pb2.ResponseInfo.FromString,
        )


class PushServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Login(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PushServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Login': grpc.unary_stream_rpc_method_handler(
          servicer.Login,
          request_deserializer=PushData__pb2.UserInfo.FromString,
          response_serializer=PushData__pb2.ResponseInfo.SerializeToString,
      ),
      'SendMessage': grpc.unary_unary_rpc_method_handler(
          servicer.SendMessage,
          request_deserializer=PushData__pb2.SendMessageInfo.FromString,
          response_serializer=PushData__pb2.ResponseInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'PushService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))