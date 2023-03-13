import time

from compas_fab.backends import RosClient
from roslibpy import Topic


def receive_message(message):
    print("Received: " + message["data"])


with RosClient("localhost") as client:
    print("Waiting for messages...")

    listener = Topic(client, "/messages", "std_msgs/String")
    listener.subscribe(receive_message)

    while client.is_connected:
        time.sleep(1)
