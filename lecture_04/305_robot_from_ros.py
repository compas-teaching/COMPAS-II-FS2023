# Before running this example, make sure to run
# "docker compose up" on the docker/gofa-noetic folder
from compas_fab.backends import RosClient

# Connect to ROS
with RosClient("localhost") as ros:
    # load the robot from ROS, but exclude its geometry
    robot = ros.load_robot(load_geometry=False)

    # robot is an instance of compas_fab.robots.Robot and it contains:
    #  - the robot model (compas.robots.RobotModel): the joints and links that make the robot
    #  - semantic information: particularly the planning groups
    #  - client: the instance of a client that connects to the robot in simulation (may not be the same client used for control)

    # Print detailed information about the robot model
    robot.info()
