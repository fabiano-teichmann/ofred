import asyncio
import time

from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage

from settings import Settings

count = 0
settings = Settings()


async def send_log(message: AbstractIncomingMessage) -> None:
    pass


async def on_message(message: AbstractIncomingMessage) -> None:
    """
    on_message doesn't necessarily have to be defined as async.
    Here it is to show that it's possible.
    """
    global count
    count = count + 1
    print(" [x] Received message %r" % message)
    print("Message body is: %r" % message.body)

    print("Before sleep!")
    await asyncio.sleep(0.5)  # Represents async I/O operations
    if count == 99999:
        raise KeyboardInterrupt
    print("After sleep!")


async def main() -> None:
    # Perform connection
    connection = await connect(
        f"amqp://{settings.user_rabbit}:{settings.passw_rabbit}@{settings.host_rabbit}:{settings.port_rabbit}")

    async with connection:
        # Creating a channel
        channel = await connection.channel()

        # Declaring queue
        queue = await channel.declare_queue(settings.queue)

        # Start listening the queue with name 'hello'
        await queue.consume(on_message, no_ack=True)

        print(" [*] Waiting for messages. To exit press CTRL+C")
        await asyncio.Future()


if __name__ == "__main__":
    start = time.perf_counter()
    try:

        asyncio.run(main())
    except KeyboardInterrupt:
        d = round(time.perf_counter() - start, 2)
        print(f"Time total {d} sec")
