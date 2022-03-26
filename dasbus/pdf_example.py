# Registrando um serviço DBus
session_bus.register_service( 
    "org.exampĺe.Chat"
)

# Publicando um objeto DBus
session_bus.publish_object(
    "/org/example/Chat/Rooms1",
    # Room()
)