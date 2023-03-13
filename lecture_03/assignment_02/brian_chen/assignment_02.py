"""Assignment 02: Build your own robot model
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Translation
from compas.robots import Configuration
from compas.robots import Joint
from compas.robots import RobotModel
from compas.geometry import Box
import Rhino.Geometry as rg
import copy
from math import radians

# create cylinder in yz plane
radius, length = 0.3, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2.0, 0, 0]))

# create a end effector
frame_ef = Frame([0.5, 0, 0], [1, 0, 0], [0, 1, 0])
width, length_ef, height = 1, 3, 0.1
box = Box(frame_ef, width, length_ef, height)

# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh1 = Mesh.from_shape(cylinder)
mesh2 = Mesh.from_shape(cylinder)
mesh3 = Mesh.from_shape(cylinder)
mesh4 = Mesh.from_shape(box)

# add links
link0 = model.add_link("world")
link1 = model.add_link("link1", visual_mesh=mesh1, visual_color=(0.2, 0.5, 0.6))
link2 = model.add_link("link2", visual_mesh=mesh2, visual_color=(0.5, 0.6, 0.2))
link3 = model.add_link("link3", visual_mesh=mesh3, visual_color=(0.3, 0.2, 0.4))
link4 = model.add_link("link4", visual_mesh=mesh4, visual_color=(0.6, 0.1, 0.5))

# add joints between the links
axis_00, axis_01, axis_02 = (0, 1, 0), (0, 0, 1), (1, 0, 0)

origin1 = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin1, axis_00)

origin2 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin2, axis_01)

origin3 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin3, axis_00)

origin4 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link3, link4, origin4, axis_02)

# Create a configuration object matching the number of joints in your model
configuration = model.zero_configuration()
configuration.joint_values = [jv_01, jv_02, jv_03, jv_04]

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)
artist_box = Artist(mesh4)

# Render everything
a = artist.draw_visual()
b = artist_box.draw()
artist.redraw()

trans = rg.Transform.Rotation(radians(50), rg.Point3d(0,0,0))
leg_01 = copy.deepcopy(a)
[r.Transform(trans) for r in leg_01]