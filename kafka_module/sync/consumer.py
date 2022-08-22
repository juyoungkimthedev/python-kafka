import json

from kafka import KafkaConsumer

# When the consumer starts, you can print out all the messages
# auto_offset_reset allows oldest message is displayed first
if __name__ == "__main__":
    consumer = KafkaConsumer(
        "python-kafka-topic", bootstrap_servers="localhost:9092", auto_offset_reset="earliest"
    )

    for message in consumer:
        print(message)
        print("------------------------")
        print(json.loads(message.value))

        # ConsumerRecord(
        #     topic="python-kafka-topic",
        #     partition=0,
        #     offset=1,
        #     timestamp=1661123429190,
        #     timestamp_type=0,
        #     key=None,
        #     value=b'{"user_id": 9, "recipient_id": 22, "message": "fCTMmNCURUKPWELufqQtkeGsjXUTnruh"}',
        #     headers=[],
        #     checksum=None,
        #     serialized_key_size=-1,
        #     serialized_value_size=81,
        #     serialized_header_size=-1,
        # )

        # {"user_id": 93, "recipient_id": 56, "message": "cvfHUbKCmbRfUCshfGDEqiewjOejzAyb"}
