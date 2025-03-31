import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    RABBIT_HOST = os.environ.get('RABBIT_HOST', default='rabbitmq')
    RABBIT_USER = os.environ.get('RABBIT_USER', default='admin')
    RABBIT_PASSWORD = os.environ.get('RABBIT_PASSWORD', default='adminpass')
    EXCHANGE_NAME = os.environ.get('EXCHANGE_NAME', default='pubsub_exchange')
    CASSANDRA_HOST = os.environ.get('CASSANDRA_HOST', default='cassandra')
    KEYSPACE = os.environ.get('CASSANDRA_KEYSPACE', default='pubsub_data')
