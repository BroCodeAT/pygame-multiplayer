from pygame_multiplayer import NetworkServerBase

server = NetworkServerBase("localhost", 1222, True)

server._accept()

print(server)
