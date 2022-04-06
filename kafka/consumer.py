# https://elasticsearch-py.readthedocs.io/en/v7.13.1/
import asyncio
from datetime import datetime
from elasticsearch import AsyncElasticsearch
from kafka import KafkaConsumer
import pymssql
import os
import json
from dotenv import load_dotenv
load_dotenv()

async def main():
    consumer = KafkaConsumer('sentiment', bootstrap_servers=['192.168.10.11:30092','192.168.10.11:30093'],
        group_id='sentiment',
        auto_offset_reset = 'earliest',
        value_deserializer=lambda m: json.loads(m)
        )
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value`
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))

    return 

loop = asyncio.get_event_loop()
loop.run_until_complete(main())