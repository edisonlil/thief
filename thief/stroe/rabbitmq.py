import pika

from thief.configuration.rabbitmq_configuration import RabbitMqConfiguration


class RabbitMq:

    config = RabbitMqConfiguration()
    connection = None
    def __init__(self):

        credentials = pika.PlainCredentials(self.config.username(),self.config.password())
        params = pika.ConnectionParameters(host=self.config.host(), port=self.config.port()
                                           ,credentials=credentials)
        self.connection = pika.BlockingConnection(params)
        pass


    def channel(self):
        return self.connection.channel()

    def create_queue(self,queue_name):
        self.channel().queue_declare(queue_name)

    def listen(self,queue_name,callback):
        channel = self.channel()
        channel.basic_consume(queue_name,callback)
        channel.start_consuming()
        pass

    def pop(self,queue_name,is_ack=False):
        self.channel().basic_get(queue_name,is_ack)

    def publish(self,exchange,queue_name,message):
        channel = self.channel()
        channel.basic_publish(exchange=exchange, routing_key=queue_name, body=message)
        pass

