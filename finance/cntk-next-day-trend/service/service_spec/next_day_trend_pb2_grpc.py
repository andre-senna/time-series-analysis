# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from service.service_spec import next_day_trend_pb2 as service_dot_service__spec_dot_next__day__trend__pb2


class NextDayTrendStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.trend = channel.unary_unary(
        '/NextDayTrend/trend',
        request_serializer=service_dot_service__spec_dot_next__day__trend__pb2.Input.SerializeToString,
        response_deserializer=service_dot_service__spec_dot_next__day__trend__pb2.Output.FromString,
        )


class NextDayTrendServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def trend(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NextDayTrendServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'trend': grpc.unary_unary_rpc_method_handler(
          servicer.trend,
          request_deserializer=service_dot_service__spec_dot_next__day__trend__pb2.Input.FromString,
          response_serializer=service_dot_service__spec_dot_next__day__trend__pb2.Output.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'NextDayTrend', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
