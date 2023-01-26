from pygame_multiplayer.commands.flags import NetworkFlag


def test_network_flags():
    assert NetworkFlag.DISCONNECTED == 100
    assert NetworkFlag.CONNECTED == 101
