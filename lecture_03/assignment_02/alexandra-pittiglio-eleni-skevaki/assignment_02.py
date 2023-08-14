"""Assignment 02: Build your own robot model
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Translation
from compas.robots import Joint
from compas.robots import RobotModel
import math

# create cylinder in yz plane
radius, length = 0.3, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2.0, 0, 0]))

# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
angles_cnt = 6
angles_cnt = max(5, angles_cnt)
link_cnt = 2 * angles_cnt
meshes = [Mesh.from_shape(cylinder) for i in range(link_cnt)]

# add links
links = [model.add_link("world")]
for i in range(link_cnt):
    angle = i//2
    link = model.add_link("link{}".format(i+1), visual_mesh=meshes[i], visual_color=((angle/(0.5*link_cnt)), 0.0, (angle/(0.5*link_cnt))))
    links.append(link)
    
# add joints between the links
axis = (0, 0, 1)
origin1 = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, links[0], links[1], origin1, axis)
origin2 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
for i in range(1,link_cnt):
    model.add_joint("joint{}".format(i+1), Joint.CONTINUOUS, links[i], links[i+1], origin2, axis)


# Create a configuration object matching the number of joints in your model
config =  model.zero_configuration()
config.joint_values = angles_cnt*[-4 * math.pi/(angles_cnt), 2 * math.pi/(angles_cnt)]

# Update the model using the artist
artist = Artist(model)
artist.update(config)

# Render everything
artist.clear_layer()
artist.draw_visual()
artist.redraw()