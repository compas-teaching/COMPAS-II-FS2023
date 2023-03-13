from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Translation
from compas.robots import Configuration
from compas.robots import Joint
from compas.robots import RobotModel
import math

# create cylinder in yz plane
radius, length = 0.3, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2.0, 0, 0]))

# create box in xy plane

box = Box(Frame.worldXY(), length, 0.5, 0.5)

# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh1 = Mesh.from_shape(cylinder)
mesh2 = Mesh.from_shape(cylinder)
mesh3 = Mesh.from_shape(cylinder)
mesh4 = Mesh.from_shape(cylinder)


# add links
link0 = model.add_link("world")
link1 = model.add_link("link1", visual_mesh=mesh1, visual_color=(0.2, 0.5, 0.6))
link2 = model.add_link("link2", visual_mesh=mesh2, visual_color=(0.5, 0.6, 0.2))
link3 = model.add_link("link3", visual_mesh=mesh3, visual_color=(0.3, 0.7, 0.3))
link4 = model.add_link("link4", visual_mesh=mesh3, visual_color=(0.4, 0.4, 0.4))


# add joints between the links
axis = (0, 0, 1)

origin = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin, axis)

origin1 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin1, axis)

origin2 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin2, axis)

origin3 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link3, link4, origin3, axis)


# Create a configuration object matching the number of joints in your model
#Creating a configuration to draw the number 2
configuration = model.zero_configuration()
configuration.joint_values = [0, -math.radians(90), math.radians(-45), math.radians(135)]

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

# Render everything
artist.draw_visual()
artist.redraw()
