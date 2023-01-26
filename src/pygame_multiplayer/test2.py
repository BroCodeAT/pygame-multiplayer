import py_mp

client = py_mp.CommandClient()

client.connect("localhost", 5000)

client.send(py_mp.ClientCommand(py_mp.commands.flags.NetworkFlag.CONNECTED, test="test"))
