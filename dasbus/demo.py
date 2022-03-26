# DasBus Library 
from dasbus.connection import SessionMessageBus, SystemMessageBus

system_bus = SystemMessageBus() # system bus init
session_bus = SessionMessageBus() # Session Bus init

proxy = session_bus.get_proxy( # specify dbus service name and path
    "org.freedesktop.systemd1",
    "/org/freedesktop/systemd1"
)

print(proxy.ListUnits()) # get property of dbus proxy

# proxy.SendMessage("Hello World!") # call a method of the DBus proxy


# def callback(message): # connect a callback to the signal of the DBus proxy and start the event loop
#     print(message)
# proxy.MessageReceived.connect(
#     callback
# )

