import pydbus

system_bus = pydbus.SystemBus()

systemd = system_bus.get(".systemd1")

for unit in systemd.ListUnits():
    print(unit)