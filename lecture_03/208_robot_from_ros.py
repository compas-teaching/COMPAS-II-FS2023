# Before running this example, ROS needs to be running
# Usually, this is done using Docker, eg. composing up on the docker
# files in the folder data/docker/robot_cell
from compas.artists import Artist
from compas_fab.backends import RosClient

with RosClient("localhost") as ros:
    robot = ros.load_robot(load_geometry=True, precision="12f")
    robot.info()

    artist = Artist(robot.model)
    artist.draw_visual()
    artist.redraw()
