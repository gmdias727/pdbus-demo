from dasbus.loop import EventLoop
loop = EventLoop()

from dasbus.connection import SessionMessageBus
session_bus = SessionMessageBus()

class HelloWorld(object):
    __dbus_xml__ = """
    <node>
        <interface name="org.example.HelloWorld">
            <method name="Hello">
                <arg direction="in" name="name" type="s" />
                <arg direction="out" name="return" type="s" />
            </method>
            <method name="World">
                <arg direction="in" name="num" type="i" />
                <arg direction="out" name="return" type="i" />
            </method>
        </interface>
    </node>
    """

    def Hello(self, name):
        return f"Hello {name}!"
    def World(self, num):
        return num

session_bus.publish_object("/org/example/HelloWorld", HelloWorld()) 
session_bus.register_service("org.example.HelloWorld")
loop.run()
