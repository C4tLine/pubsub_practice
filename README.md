## Project info
Program Language - Python  
Database - Apache Cassandra     
Message broker - RabbitMQ

## Set up and run

1. Clone this repository:
```bash
git clone https://github.com/Rubsun/subpub_cassandra
```

2. Enter directory with project:
```bash
cd pubsub_practice
```

3. Create or replace .env file with custom settings:
```bash
RABBIT_HOST=        *your_host*
RABBIT_USER=        *your_user*
RABBIT_PASSWORD=    *your_password*
EXCHANGE_NAME=      *your_exchange*
CASSANDRA_HOST=     *your_host*
CASSANDRA_KEYSPACE= *your_data*
```

4. Run docker-compose:
```bash
docker-compose up --build
```

## For development

1. Create python virtual environment via command:
```
python -m venv venv
```

2. Activate venv and install requirements from req.txt file:
- On Linux
```
./venv/bin/activate
pip install -r req.txt
```
- On Windows
```
./venv/Scripts/activate
pip install -r req.txt
```

### Online resources/information used:
- RabbitMQ Publish/Subscribe tutorial:  
https://www.rabbitmq.com/tutorials/tutorial-three-python
- Python library pika for rabbitmq: 
https://pypi.org/project/pika/
- Cassandra quickstart tutorial:    
https://cassandra.apache.org/doc/latest/cassandra/getting-started/cassandra-quickstart.html