import json

import pika

import faker

from models import Contact


def fill_data_in_db(cnt: int):
    fake = faker.Faker()
    for i in range(cnt):
        Contact(fullname=fake.name(), email=fake.email(), msg_text=fake.text()).save()


def fill_queue_from_db():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange='email_mock', exchange_type='direct')
    channel.queue_declare(queue='email_queue', durable=True)
    channel.queue_bind(exchange='email_mock', queue='email_queue')

    contacts = Contact.objects(was_send=False)
    for c in contacts:
        message = {"id": str(c.pk)}
        channel.basic_publish(
            exchange='email_mock',
            routing_key='email_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
    connection.close()


if __name__ == '__main__':
    fill_data_in_db(500)
    fill_queue_from_db()