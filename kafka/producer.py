from kafka import KafkaProducer
from kafka.errors import KafkaError
from json import dumps
import asyncio
from random import randrange

def main(data):
    producer = KafkaProducer(bootstrap_servers=['192.168.10.11:30092','192.168.10.11:30093'],
                            value_serializer=lambda x: 
                            dumps(x).encode('utf-8'))

    # Asynchronous by default
    # future = producer.send('sentiment', key=b'data', value=data)
    future = producer.send('sentiment', key=b'data', value=data, partition=randrange(2))

    # Block for 'synchronous' sends
    record_metadata = future.get(timeout=10)

    # Successful result returns assigned partition and offset
    print (record_metadata.topic)
    print (record_metadata.offset)
    return

if __name__ == "__main__":
    data = {"data": {"aglsdajfew": """sdjf'sd\+%:)/sdaf*-1'^57"793é3jf"""}}
    main(data)