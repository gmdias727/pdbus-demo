import pydbus


session_bus = pydbus.SessionBus()
terminal = session_bus.get("org.gnome.Terminal")
terminal.Open("/home/hansolo/teste", "test", pydbus.Variant('s', 'i'))