# import asyncio
# from elasticsearch import AsyncElasticsearch
#
# from elasticsearch.helpers import async_streaming_bulk
#
# es = AsyncElasticsearch(hosts='http://localhost:9200')


"""
def connect_elk(settings: SettingsEventStore):
    global elk
    global confs
    use_ssl = False if settings.environment == "local" else True
    scheme = "http" if settings.environment == "local" else "https"
    elk = Elasticsearch(
        settings.elk_host,
        http_auth=(settings.elk_user, settings.elk_password),
        scheme=scheme,
        use_ssl=use_ssl,
    )
    confs = settings
    create_index(elk, settings)


def create_index(elk, settings):
    global index_name
    index_name = (f"{settings.elk_index}_{datetime.now().year}_{datetime.now().month}")
    elk.indices.create(index=index_name, ignore=400)
"""
import uuid

from elasticsearch import Elasticsearch

# async def gendata():
#     mywords = ['foo', 'bar', 'baz']
#     for word in mywords:
#         yield {
#             "_index": "mywords",
#             "word": word,
#         }
#
# async def main():
#     async for ok, result in async_streaming_bulk(es, gendata()):
#         action, result = result.popitem()
#         if not ok:
#             print("failed to %s document %s")
use_ssl = False
scheme = "http"
elk = Elasticsearch(
    'http://127.0.0.1:9200',
)


def send_elk():
    elk.indices.create(index="test_index", ignore=400)
    _id = str(uuid.uuid4())
    elk.create(index="test_index", id=_id, body={"ola": "ola"})


if __name__ == "__main__":
    send_elk()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
