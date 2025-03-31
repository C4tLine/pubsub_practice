from time import sleep

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

from src.common.config import Config

provider: str = 'cassandra'


class Database:
    def __init__(self, table_name: str) -> None:
        self.config: type = Config()
        self.table: str = table_name

        auth_provider = PlainTextAuthProvider(
            username=provider,
            password=provider
        )

        for _ in range(5):
            try:
                self.cluster = Cluster(
                    [self.config.CASSANDRA_HOST],
                    auth_provider=auth_provider
                )
                self.session = self.cluster.connect(self.config.KEYSPACE)
                break
            except Exception as error:
                print(f"Connection failed: {str(error)}, retrying")
                sleep(5)
        else:
            raise RuntimeError("Couldn't connect to Cassandra")

    def save_message(self, message: str) -> None:
        query = f"""
        INSERT INTO {self.table} 
        (message_id, content, created)
        VALUES (now(), %s, toTimestamp(now()))
        """
        self.session.execute(query, (message,))
