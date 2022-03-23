import pydbus


session_bus = pydbus.SessionBus()

nautilus = session_bus.get(".Nautilus")

nautilus = session_bus.CreateFolder('/home/hansolo/Desktop/z')

nautilus.Open("/home/hansolo/teste", "test", pydbus.Variant('s,', 1))


