from dataclasses import dataclass as _dc
import socket as _sock


@_dc
class ClientBase:
    socket: _sock.socket
    address: str
    port: int

    @classmethod
    def from_accept(cls, socket: _sock.socket, addr: tuple[str, int]):
        return cls(socket, addr[0], addr[1])
