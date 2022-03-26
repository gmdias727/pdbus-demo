from dasbus.loop import EventLoop
loop = EventLoop()

from dasbus.connection import SessionMessageBus
bus = SessionMessageBus()

class HelloWorld(object):
    __dbus_xml__ = """
    <node>
        <interface name="org.example.HelloWorld">
            <method name="Hello">
                <arg direction="in" name="name" type="s" />
                <arg direction="out" name="return" type="s" />
            </method>
        </interface>
    </node>
    """

    def Hello(self, name):
        return "Hello {}!".format(name)

bus.publish_object("/org/example/HelloWorld", HelloWorld())
bus.register_service("org.example.HelloWorld")
loop.run()