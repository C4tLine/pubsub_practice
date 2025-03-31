from time import sleep

from pika import PlainCredentials, BlockingConnection, ConnectionParameters, BasicProperties

from src.common.config import Config


class Publisher:
    def __init__(self) -> None:
        self.config: type = Config()
        self.connection = None
        self.channel = None

    def connect(self) -> None:
        credentials = PlainCredentials(
            self.config.RABBIT_USER,
            self.config.RABBIT_PASSWORD
        )
        self.connection = BlockingConnection(
            ConnectionParameters(
                host=self.config.RABBIT_HOST,
                credentials=credentials
            )
        )
        self.channel = self.connection.channel()
        self._setup_exchange()

    def _setup_exchange(self) -> None:
        self.channel.exchange_declare(
            exchange=self.config.EXCHANGE_NAME,
            exchange_type='fanout',
            durable=True
        )

    def publish(self, message) -> None:
        self.channel.basic_publish(
            exchange=self.config.EXCHANGE_NAME,
            routing_key='',
            body=message.encode(),
            properties=BasicProperties(
                delivery_mode=2
            )
        )

    def run(self) -> None:
        try:
            self.connect()
            with open('/app/input.txt', 'r') as file:
                while True:
                    line = file.readline()
                    if not line:
                        sleep(2)
                        file.seek(0)
                        continue

                    self.publish(line.strip())
                    print(f"[PUB] Sent: {line.strip()}")
                    sleep(0.1)
        except Exception as error:
            print(f"Error: {str(error)}")
        finally:
            if self.connection:
                self.connection.close()


if __name__ == "__main__":
    Publisher().run()
