import json

from aio_pika import Message, connect

from settings import Settings


async def publisher(message: dict) -> None:
    # Perform connection
    settings = Settings()
    url_conn = f"amqp://{settings.user_rabbit}:{settings.passw_rabbit}@{settings.host_rabbit}:{settings.port_rabbit}"
    connection = await connect(url_conn)

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("hello")
        await channel.default_exchange.publish(
            Message(content_type='application/json', body=json.dumps(message).encode()), routing_key=queue.name,
        )
