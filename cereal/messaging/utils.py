import os

ZMQ_PROTOCOLS = {
  "SHARED_MEMORY": "inproc://",
  "INTER_PROCESS": "ipc://@",
  "TCP": "tcp://",
}


def get_zmq_protocol() -> str:
  default_protocol = ZMQ_PROTOCOLS["TCP"]
  override = os.getenv("ZMQ_MESSAGING_PROTOCOL")
  if override in ZMQ_PROTOCOLS:
    return ZMQ_PROTOCOLS[override]
  return default_protocol


def get_address() -> str:
  return os.getenv("ZMQ_MESSAGING_ADDRESS", "127.0.0.1")


def get_zmq_socket_path(endpoint: str) -> str:
  return f"{get_zmq_protocol()}{get_address()}:{endpoint}"
