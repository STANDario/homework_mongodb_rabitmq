from faker import Faker
import pika

from src.model import Contact
from src.db import connect


fake = Faker("uk-UA")

NUMBER_CONTACTS = 15


def seed():
    for i in range(NUMBER_CONTACTS):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        address = fake.address()

        Contact(fullname=name, email=email, phone=phone, address=address).save()


def main():
    credentials = pika.PlainCredentials("guest", "guest")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
    chanel = connection.channel()

    chanel.exchange_declare(exchange="task-mock", exchange_type="direct")
    chanel.queue_declare(queue="contact", durable=True)
    chanel.queue_bind(exchange="task-mock", queue="contact")

    contacts = Contact.objects()

    for contact in contacts:
        contact_id = contact.to_mongo().to_dict().get("_id")

        chanel.basic_publish(exchange="task-mock", routing_key="contact", body=str(contact_id).encode(),\
                             properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))

    connection.close()


if __name__ == '__main__':
    seed()
    main()

    # Contact.objects().delete()
