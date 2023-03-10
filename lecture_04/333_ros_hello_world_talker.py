import time

from compas_fab.backends import RosClient
from roslibpy import Topic

count = 0

with RosClient("localhost") as client:
    talker = Topic(client, "/messages", "std_msgs/String")
    talker.advertise()

    while client.is_connected:
        count += 1
        msg = "Hello #{}".format(count)

        talker.publish({"data": msg})
        print("Sent: " + msg)

        time.sleep(1)

    talker.unadvertise()
