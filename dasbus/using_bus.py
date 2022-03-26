from dasbus.connection import SessionMessageBus
bus = SessionMessageBus()

proxy = bus.get_proxy(
    "org.example.HelloWorld",
    "/org/example/HelloWorld"
)

print(proxy.Hello('fodase'))
print(proxy.World(555555))

print(type(proxy.World(555555)))