import configparser


class RabbitMqConfiguration:


    config_file = "./thief.ini"

    name = "rabbitmq"

    config = None

    def __init__(self):

        self.config = configparser.ConfigParser()
        self.config.read(self.config_file, encoding="utf-8")
        pass

    def host(self):
        return self.config.get(self.name,"host")

    def port(self):
        return self.config.get(self.name,"port")

    def username(self):
        return self.config.get(self.name, "username")

    def password(self):
        return self.config.get(self.name,"password")

