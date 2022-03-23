from dasbus.connection import SessionMessageBus
# dbus library in python 
# system_bus = SystemMessageBus() # system bus init
session_bus = SessionMessageBus() # Session Bus init
print(session_bus)

# proxy = session_bus.get_proxy( # specify dbus service name and path
#     "org.example.Chat",
#     "/org/example/Chat/Rooms/3"
# )

# print(proxy.Name) # get property of dbus proxy

# proxy.SendMessage("Hello World!") # call a method of the DBus proxy


# def callback(message): # connect a callback to the signal of the DBus proxy and start the event loop
#     print(message)
# proxy.MessageReceived.connect(
#     callback
# )

