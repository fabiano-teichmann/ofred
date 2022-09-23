import json

import pika

from common.dto import DTOLog
from settings import Settings

from app.models import Events


def publisher(dto_log: DTOLog) -> bool:
    settings = Settings()
    url = f"amqp://{settings.user_rabbit}:{settings.passw_rabbit}@{settings.host_rabbit}:{settings.port_rabbit}"
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(settings.queue)
    channel.basic_publish(exchange='', routing_key=settings.queue,
                          body=dto_log.json().encode(),
                          properties=pika.BasicProperties(content_type="application/json"))
    connection.close()
    return True


def send_event_log(event: Events):
    data = {"app": event.application_tbl.name, "domain": event.domain_tbl.name, "req_event": event.event_name,
            "req_path": event.req_path, "req_body": json.dumps(json.loads(event.req_body)),
            "resp_body": json.dumps(json.loads(event.resp_body)),
            "status_code": 200, "dt_current_timestamp": event.changed_on}

    dto_log = DTOLog(**data)
    publisher(dto_log)

