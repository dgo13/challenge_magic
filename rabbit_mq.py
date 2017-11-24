import pika
import pymysql
from playhouse.shortcuts import *
import json

class RabbitMq(): 
    routing_key = 'moving_cards'
    exchange = 'cards'
    exchange_type='direct'
    host='localhost'

    def send(cards):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RabbitMq.host))
        channel = connection.channel()
        channel.exchange_declare(exchange=RabbitMq.exchange,
                                exchange_type=RabbitMq.exchange_type)

        for c in cards:
            card = model_to_dict(c)
            card_json = json.dumps(card)
            message = card_json

            channel.basic_publish(exchange=RabbitMq.exchange,
                                routing_key=RabbitMq.routing_key,
                                body=message)
        connection.close()

    def receive(callback):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RabbitMq.host))
        channel = connection.channel()

        channel.exchange_declare(exchange=RabbitMq.exchange,
                                exchange_type=RabbitMq.exchange_type)

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange=RabbitMq.exchange,
                            queue=queue_name,
                            routing_key=RabbitMq.routing_key)

        print(' [*] Waiting for cards. To exit press CTRL+C')

        channel.basic_consume(callback,
                            queue=queue_name,
                            no_ack=True)
        channel.start_consuming()
