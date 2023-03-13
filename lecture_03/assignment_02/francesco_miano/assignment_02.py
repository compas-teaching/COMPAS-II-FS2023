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

# create cylinder in yz plane

#cylinders
radius, length = 0.4, 4
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2.0, 0, 0]))

radius_2, length_2 = 0.6, 8
body = Cylinder(Circle(Plane([0, 0, 0], [0, 0, 1]), radius_2), length_2)
body.transform(Translation.from_vector([0,0,-length_2/2]))

# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh_1 = Mesh.from_shape(cylinder)
mesh_2 = Mesh.from_shape(body)

# add LINK
link0 = model.add_link("world")
#arms
link1_A = model.add_link("link1_A", visual_mesh=cylinder, visual_color=(0.2, 0.5, 0.6))
link2_A = model.add_link("link2_A", visual_mesh=cylinder, visual_color=(0.1, 0.6, 0.2))
link1_B = model.add_link("link1_B", visual_mesh=cylinder, visual_color=(0.5, 0.2, 0.2))
link2_B = model.add_link("link2_B", visual_mesh=cylinder, visual_color=(0.5, 0.9, 0.2))
# body
body = model.add_link("link_body", visual_mesh=body, visual_color=(0.5, 0.9, 0.2))
# legs
leg_1 = model.add_link("leg_1", visual_mesh=cylinder, visual_color=(0.5, 0.9, 0.2))
leg_2 = model.add_link("leg_2", visual_mesh=cylinder, visual_color=(0.5, 0.9, 0.2))

# add JOINTS between the links
axis = (0, 1, 0)
# arm right
origin = Frame([0, 0, 0], [1, 0, 0], [0, 1, 0])
model.add_joint("joint0_A", Joint.CONTINUOUS, link0, link1_A, origin, axis)
origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint1_A", Joint.CONTINUOUS, link1_A, link2_A, origin, axis)
# arm left
origin = Frame([0, 0, 0], [-1, 0, 0], [0, 1, 0])
model.add_joint("joint0_B", Joint.CONTINUOUS, link0, link1_B, origin, axis)
origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint1_B", Joint.CONTINUOUS, link1_B, link2_B, origin, axis)
# body
origin = Frame((0, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("body", Joint.CONTINUOUS, link0, body, origin, axis)
# legs
origin = Frame((0, 0, -8), (1, 0, 0), (0, 1, 0))
model.add_joint("leg_1", Joint.CONTINUOUS, body, leg_1, origin, axis)
origin = Frame((0, 0, -8), (-1, 0, 0), (0, 1, 0))
model.add_joint("leg_2", Joint.CONTINUOUS, body, leg_2, origin, axis)

# Create a configuration object matching the number of joints in your model
configuration = model.zero_configuration() #close to all zeros
configuration.joint_values =[a,b,0,c,d,e,f]

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

a = artist.draw_visual()
print(model)
