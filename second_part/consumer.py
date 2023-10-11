import sys
from time import sleep
from bson import ObjectId

import pika

from src.model import Contact
from src.db import connect


credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
chanel = connection.channel()

contacts = Contact.objects()

chanel.queue_declare(queue="contact", durable=True)


def callback(ch, method, properties, body):
    object_id = ObjectId(body.decode())
    contact = contacts(id=object_id)
    print(f"Send to: {contact[0].to_mongo().to_dict().get('fullname')}")
    contact.update(send=True)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    sleep(0.5)


chanel.basic_qos(prefetch_count=1)
chanel.basic_consume(queue="contact", on_message_callback=callback)


if __name__ == '__main__':
    chanel.start_consuming()

