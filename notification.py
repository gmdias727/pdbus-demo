import pydbus

session_bus = pydbus.SessionBus() # <pydbus.bus.Bus object at 0x7f1ee6bc1040>
system_bus = pydbus.SystemBus() # <pydbus.bus.Bus object at 0x7f1ee6b82a90>

notifications = session_bus.get("org.freedesktop.Notifications")
notifications.Notify("test", 0, "dialog-information", "Hello World!", "pydbus works :)", [], {}, 5000)

# system_bus = 

system_operations = session_bus.get("org.freedesktop.systemd1") 
# <DBUS.
# <CompositeObject>(org.freedesktop.systemd1.Manager+org.freedesktop.DBus.Peer+org.freedesktop.DBus.Introspectable+org.freedesktop.DBus.Properties) 
# object at 0x7f19cf5ffcd0>
# print(system_operations)

system_operations.Reboot() 

# print(notifications)