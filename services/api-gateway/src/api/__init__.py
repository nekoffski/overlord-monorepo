import grpc

from overlord.log import log
from overlord import proto, interceptor

from . import stats


async def start(stats_proxy):
    listen_addr = "[::]:5555"
    log.info("Starting grpc server on: {}", listen_addr)

    server = grpc.aio.server(interceptors=(interceptor.RequestLogger(log),))
    server.add_insecure_port(listen_addr)

    proto.register_pinger_service(server)
    stats.register_statistics_provider_service(server, stats_proxy)

    await server.start()
    await server.wait_for_termination()
