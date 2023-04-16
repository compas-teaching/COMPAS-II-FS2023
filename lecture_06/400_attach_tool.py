import os
import time

from compas_fab.backends import RosClient
from compas_fab.robots import Tool

from compas.datastructures import Mesh
from compas.geometry import Frame

HERE = os.path.dirname(__file__)

# create tool from mesh and frame
mesh = Mesh.from_stl(os.path.join(HERE, "vacuum_gripper.stl"))
tool = Tool(mesh, Frame([0, 0, 0.07], [1, 0, 0], [0, 1, 0]))

with RosClient("localhost") as client:
    robot = client.load_robot()
    config = robot.zero_configuration()
    print(robot.forward_kinematics(config))

    # Attach the tool
    robot.attach_tool(tool)

    print(robot.forward_kinematics(config))

    time.sleep(1)
