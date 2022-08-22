import json
import random
import string
import time
from datetime import datetime

from kafka import KafkaProducer

user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))


def generate_message() -> dict:
    random_user_id = random.choice(user_ids)

    recipient_ids_copy = recipient_ids.copy()
    recipient_ids_copy.remove(random_user_id)

    random_recipient_id = random.choice(recipient_ids_copy)

    message = "".join(random.choice(string.ascii_letters) for _ in range(32))

    return {"user_id": random_user_id, "recipient_id": random_recipient_id, "message": message}


# The kafka topic we created for this demo is called 'python-kafka-topic'
# Messages going into Kafka need to be serialised as json
def serializer(message):
    return json.dumps(message).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=serializer)


if __name__ == "__main__":
    # Runs until you kill the program
    while True:
        dummy_message = generate_message()

        # Send to our topic 'python-kafka-topic'
        print(f"Producing message @ {datetime.now()} | Message = {str(dummy_message)}")

        # Value must be bytes type or serializable via value_serializer
        producer.send(topic="python-kafka-topic", value=dummy_message)

        # Sleep for some seconds to reduce overload
        time_to_sleep = random.randint(1, 6)
        time.sleep(time_to_sleep)
