import time

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

from src.common.config import Config


class Database:
    def __init__(self, table_name):
        self.config = Config()
        self.table = table_name

        auth_provider = PlainTextAuthProvider(
            username='cassandra',
            password='cassandra'
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
                time.sleep(5)
        else:
            raise RuntimeError("Couldn't connect to Cassandra")

    def save_message(self, message):
        query = f"""
        INSERT INTO {self.table} 
        (message_id, content, created)
        VALUES (now(), %s, toTimestamp(now()))
        """
        self.session.execute(query, (message,))
