import os


LOG_LEVEL = os.getenv("LOG_LEVEL")

API_GATEWAY_HOST = os.getenv("API_GATEWAY_HOST")
API_GATEWAY_GRPC_PORT = int(os.getenv("API_GATEWAY_GRPC_PORT"))

DEVICE_GATEWAY_HOST = os.getenv("DEVICE_GATEWAY_HOST")
DEVICE_GATEWAY_GRPC_PORT = int(os.getenv("DEVICE_GATEWAY_GRPC_PORT"))

LOG_SERVER_HOST = os.getenv("LOG_SERVER_HOST")
LOG_SERVER_GRPC_PORT = int(os.getenv("LOG_SERVER_GRPC_PORT"))
LOG_SERVER_LOGGER_PORT = int(os.getenv("LOG_SERVER_LOGGER_PORT"))

YEELIGHT_CONNECTOR_HOST = os.getenv("YEELIGHT_CONNECTOR_HOST")
YEELIGHT_CONNECTOR_GRPC_PORT = int(os.getenv("YEELIGHT_CONNECTOR_GRPC_PORT"))