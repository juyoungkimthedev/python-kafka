# python-kafka
Playing around with Kafka locally using Docker and Python

Create kafka topics by executing inside kafka broker container.
Normally kafka topics are created in Confluent https://www.confluent.io/.
When you docker-compose up the kafka instance locally, run the below command to execute inside the broker:

`docker-compose up --build`

`docker exec -it kafka /bin/sh`

All Kafka shell scripts are located inside `/opt/kafka_<version>/bin`

## Below commands are useful commands for dealing with topics in kafka

Create topic:

- `kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic <name of kafka topic>`

List topics:

- `kafka-topics.sh --list --zookeeper zookeeper:2181`

Describe a topic:

- `kafka-topipcs.sh --describe --zookeeper zookeeper:2181 --topic <name of kafka topic>`

Delete a topic:

- `kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic <name of kafka topic>`


## Producer and Consumers

To produce a message to a topic:

- `kafka-console-producer.sh --broker-list kafka:9092 --topic <name of topic>`

Then a console pops up and you can send a message `> {'user_id': 1234, 'message': 'Hi'}`

To consume a message:

- `kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic <name of topic>`

Note that you need to have consumer opened at all times to see the incoming messages

To list all producer messages in a topic:

- `kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic <name of topic> --from-beginning`