import pydbus

session_bus = pydbus.SessionBus()
system_bus = pydbus.SystemBus()

notifications = session_bus.get(".Notifications")
notifications.Notify("test", 0, "dialog-information", "Hello World!", "pydbus works :)", [], {}, 5000)

system_operations = session_bus.get("org.freedesktop.systemd1")

system_operations.Reboot()