z  # Before running this example, make sure to run
# "docker compose up" on the docker/gofa-noetic folder
from compas.artists import Artist
from compas_fab.backends import RosClient

# Connect to ROS
with RosClient("localhost") as ros:
    # load the robot from ROS including its geometry,
    # use a high precision value (meshes are in meters) otherwise COMPAS will weld vertices
    robot = ros.load_robot(load_geometry=True, precision="12f")
    robot.artist = Artist(robot.model)

robot.artist.draw_visual()
robot.artist.redraw()
