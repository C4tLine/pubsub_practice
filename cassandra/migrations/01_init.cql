CREATE KEYSPACE IF NOT EXISTS pubsub_data
WITH REPLICATION = {
    'class' : 'NetworkTopologyStrategy',
    'replication_factor' : 1
};

CREATE TABLE IF NOT EXISTS pubsub_data.messages_first (
    message_id timeuuid PRIMARY KEY,
    content text,
    created timestamp
);

CREATE TABLE IF NOT EXISTS pubsub_data.messages_second (
    message_id timeuuid PRIMARY KEY,
    content text,
    created timestamp
);