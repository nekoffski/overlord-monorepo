
import grpc

from overlord import proto, interceptor, cfg
from overlord.log import log


class DeviceGateway(proto.DeviceGatewayServicer):
    yeelight_endpoint = f'{cfg.YEELIGHT_CONNECTOR_HOST}:{
        cfg.YEELIGHT_CONNECTOR_GRPC_PORT}'

    async def discover_devices(
        self,
        request: proto.DiscoverDevicesRequest,
        context: grpc.aio.ServicerContext,
    ) -> proto.Devices:
        async with grpc.aio.insecure_channel(self.yeelight_endpoint) as channel:
            return await proto.YeelightConnectorStub(channel).discover_devices(request)

    async def get_devices(
        self,
        request: proto.GetDevicesRequest,
        context: grpc.aio.ServicerContext,
    ) -> proto.Devices:
        async with grpc.aio.insecure_channel(self.yeelight_endpoint) as channel:
            return await proto.YeelightConnectorStub(channel).get_devices(request)


def register_device_gateway_service(server):
    proto.add_DeviceGatewayServicer_to_server(
        DeviceGateway(), server)


async def start():
    listen_addr = f"[::]:{cfg.DEVICE_GATEWAY_GRPC_PORT}"
    log.info("Starting grpc server on: {}", listen_addr)

    server = grpc.aio.server(interceptors=(
        interceptor.RequestLogger(log, filters=['ping']),))
    server.add_insecure_port(listen_addr)

    proto.register_pinger_service(server)
    register_device_gateway_service(server)

    await server.start()
    await server.wait_for_termination()
