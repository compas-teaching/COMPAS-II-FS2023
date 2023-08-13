"""Assignment 02: Build your own robot model
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Sphere
from compas.geometry import Translation
from compas.robots import Configuration
from compas.robots import Joint
from compas.robots import RobotModel

# create cylinder in yz plane
radius, length = 0.3, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2.0, 0, 0]))

# create boxes
len_xz = 0.5
len_y = 12
box1 = Box(Frame.worldXY(), len_xz, len_y, len_xz)

# create sphere
rad_ball = 0.8
sphere = Sphere([0, 0, 0], rad_ball)

# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh0 = Mesh.from_shape(sphere)
mesh1 = Mesh.from_shape(cylinder)
mesh2 = Mesh.from_shape(cylinder)
mesh3 = Mesh.from_shape(box1)

# add links
link_base = model.add_link("world")
link0 = model.add_link("link0", visual_mesh=mesh0, visual_color=(0.1, 0.2, 0.7))
link1 = model.add_link("link1", visual_mesh=mesh1, visual_color=(0.6, 0.2, 0.6))
link2 = model.add_link("link2", visual_mesh=mesh2, visual_color=(0.9, 0.2, 0.4))
link3 = model.add_link("link3", visual_mesh=mesh3, visual_color=(0.7, 0.9, 0.2))

# add joints between the links
axis0 = (0, 0, 1)
origin0 = Frame.worldXY()
model.add_joint("joint0", Joint.CONTINUOUS, link_base, link0, origin0, axis0)

axis1 = (0, 0, 1)
origin1 = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin1, axis1)

axis2 = (0, 1, 0)
origin2 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin2, axis2)

origin3 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
axis3 = (0, 1, 0)
limit_prismatic = [-len_y + 2, len_y - 2]
model.add_joint("joint3", Joint.PRISMATIC, link2, link3, origin3, axis3, limit_prismatic)

# Create a configuration object matching the number of joints in your model
configuration = Configuration([angle1, angle2, stroke], [Joint.CONTINUOUS, Joint.CONTINUOUS, Joint.PRISMATIC], ["joint1", "joint2", "joint3"])

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

# Render everything
a = artist.draw_visual()
artist.redraw()