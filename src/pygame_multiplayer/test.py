import py_mp

server = py_mp.CommandServer()

server.bind("localhost", 5000)

server.accept(1)

print(server.recv(server.clients[0]))
