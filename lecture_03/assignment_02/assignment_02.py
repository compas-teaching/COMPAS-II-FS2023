"""Assignment 02: Build your own robot model
"""
import math
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Box
from compas.geometry import Translation
from compas.robots import Joint
from compas.robots import RobotModel
from compas.geometry import boolean_union_mesh_mesh,boolean_difference_mesh_mesh

# Create cylinder in a plane
radius, c_length = 0.3, 5.0
cylinder = Cylinder(Circle(Plane([0, 0, 0], [0, 0, 1]), radius), c_length)
cylinder.transform(Translation.from_vector([0, 0, c_length / 2.0]))

# Create an other cylinder as a 'pizza holder'
cylinder_2 = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius * 10.0), c_length * 0.1)
cylinder_2.transform(Translation.from_vector([0, 0, c_length]))

# Create a boxes for the 'piston'
b_length = 10
box = Box(Frame.worldXY(), 0.2, 0.2, b_length)
box.transform(Translation.from_vector([0, 0, b_length / 2.0]))

box_2 = Box(Frame.worldXY(), 0.5,0.5, b_length)
box_2.transform(Translation.from_vector([0, 0, b_length / 2.0]))

# Create robot model
model = RobotModel("robot", links=[], joints=[])

# Link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh1 = Mesh.from_shape(cylinder,triangulated=True)

vertices_and_faces = boolean_difference_mesh_mesh(
    Mesh.from_shape(box_2,triangulated=True).to_vertices_and_faces(), Mesh.from_shape(box,triangulated=True).to_vertices_and_faces()
)
mesh2 =  Mesh.from_vertices_and_faces(*vertices_and_faces)

mesh3 = Mesh.from_shape(box)

vertices_and_faces = boolean_union_mesh_mesh(
    mesh1.to_vertices_and_faces(), Mesh.from_shape(cylinder_2,triangulated=True).to_vertices_and_faces()
)
mesh4= Mesh.from_vertices_and_faces(*vertices_and_faces)

# Add links
link0 = model.add_link("world")
link1 = model.add_link("link1", visual_mesh=mesh1, visual_color=(0.2, 0.5, 0.6))
link2 = model.add_link("link2", visual_mesh=mesh2, visual_color=(0.5, 0.6, 0.2))
link3 = model.add_link("link3", visual_mesh=mesh3, visual_color=(0.5, 0.7, 0.3))
link4 = model.add_link("link4", visual_mesh=mesh4, visual_color=(1.0, 1.0, 1.0))

# Add joints between the links
axis1 = (0, 0, 1)
origin1 = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin1, axis1)

axis2 = (0, 1, 0)
origin2 = Frame((0, 0, c_length), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin2, axis2)

axis3 = (0, 0, 1)
origin3 = Frame((0, 0, b_length), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.PRISMATIC, link2, link3, origin3, axis3, limit=(-b_length, 0))

axis4 = (0, 1, 0)
origin4 = Frame((0, 0, b_length), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link3, link4, origin4, axis4)

# Create a configuration object matching the number of joints in your model
configuration = model.zero_configuration()
configuration.joint_values = [0.06, 0.87, -7.60, 0.75]
# Alternatively, using 'x', 'y' and 'z' in Grasshopper as params for:
# configuration.joint_values = [x, y, z, math.pi / 2 - y]

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

# Render everything
artist.draw_visual()
artist.redraw()
# outTemp = artist.draw()

