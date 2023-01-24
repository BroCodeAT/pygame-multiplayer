import socket as _sock
from ..models import ClientBase as _ClientBase


class NetworkServerBase:
    def __init__(self, host: str | None = None, port: int | None = None, auto_bind: bool = True) -> None:
        """
        Initializes all the variables in the class and prepares them for use.

        Parameters
        ----------
            host: str | None, by default None
                Specify the hostname of the server to bind to
            port: int | None, by default None
                Specify the port to bind to
            auto_bind: bool, by default True
                Automatically bind the socket to a port and host
        """
        self.conn: _sock.socket = _sock.socket(_sock.AF_INET, _sock.SOCK_STREAM)
        self._binded: bool = False
        self.addr: tuple[str, int] | None = None
        self.clients: list[_ClientBase] = []

        # Auto-bind
        if auto_bind:
            if host and port:
                self.bind(host, port)

    def __repr__(self) -> str:
        return f"<NetworkServerBase {f'binded ({self.addr[0]}:{self.addr[1]})' if self.is_binded() else 'not binded'}>"

    def bind(self,  host: str, port: int) -> _sock.socket:
        """Bind the socket to a host and port

        Parameters
        ----------
        host : str
            The Hostname or IP address to bind the server to
        port : int
            The Port to bind the server to

        Returns
        -------
        socket.socket
            The socket object that is binded to the given host and port
        """
        self.addr = (host, port)
        self.conn.bind(self.addr)
        self._binded = True
        return self.conn

    def _accept(self, amount: int = 1) -> None:
        """Wrapper of the socket.accept() method including a check if the socket is binded to a host and port
        
        Parameters
        ----------
        amount : int, by default 1
            The amount of clients to accept

        Raises
        ------
        ConnectionError
            The socket is not binded to a host and port
        """
        if not self.is_binded():
            raise ConnectionError("Not binded to any addr")
        self.conn.listen(amount)
        while len(self.clients) < amount:
            self.clients.append(_ClientBase.from_accept(*self.conn.accept()))

    def _recv(self, size: int) -> bytes:
        """Wrapper of the socket.recv() method including a check if the socket is binded to a host and port

        Parameters
        ----------
        size : int
            The amount of bytes to receive

        Returns
        -------
        bytes
            The received bytes

        Raises
        ------
        ConnectionError
            The socket is not binded to a host and port
        """
        if not self.is_binded():
            raise ConnectionError("Not binded to any addr")
        return self.conn.recv(size)

    def _send(self, data: bytes) -> None:
        """Wrapper of the socket.send() method including a check if the socket is binded to a host and port

        Parameters
        ----------
        data : bytes
            The data to send to the client

        Raises
        ------
        ConnectionError
            The socket is not binded to a host and port
        """
        if not self.is_binded():
            raise ConnectionError("Not binded to any addr")
        self.conn.send(data)

    def is_binded(self) -> bool:
        """Check if the socket is binded to a host and port

        Returns
        -------
        bool
            True if the socket is binded to a host and port, False if not
        """
        return self._binded
