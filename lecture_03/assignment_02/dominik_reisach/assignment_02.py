from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Circle
from compas.geometry import Box
from compas.geometry import Sphere
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Cone
from compas.geometry import Point
from compas.robots import Configuration
from compas.robots import Joint
from compas.robots import RobotModel
import math

# box
frame = Frame([0, 0, 0], [0, 1, 0], [0, 0, 1])
box_length = 1.0
box = Box(frame, 0.25, 0.5, box_length)

# cylinder
cyl_length = 1.5
circle = Circle(Plane([0, 0, 0], [1, 0, 0]), 0.1)
cylinder = Cylinder(circle, cyl_length)

cone_length = 1.0
cone = Cone(circle, cone_length)

point = Point(0, 0, 0)
radius = 0.2
sphere = Sphere(point, radius)


# create robot model
model = RobotModel("robot", links=[], joints=[])


# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh_box = Mesh.from_shape(box)
mesh_cone = Mesh.from_shape(cone)
mesh_cylinder = Mesh.from_shape(cylinder)
mesh_sphere = Mesh.from_shape(sphere)


# add links
link0 = model.add_link("world")
link1 = model.add_link("link1", visual_mesh=mesh_box, visual_color=(0.1, 0.2, 0.2))
link2 = model.add_link("link2", visual_mesh=mesh_cylinder, visual_color=(0.2, 0.4, 0.4))
link3 = model.add_link("link3", visual_mesh=mesh_cone, visual_color=(0.3, 0.6, 0.6))
link4 = model.add_link("link4", visual_mesh=mesh_sphere, visual_color=(0.4, 0.8, 0.8))


# add joints between the links
axis = (0, 1, 0)

origin = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin, axis)

origin_1 = Frame((box_length / 2 + cyl_length / 2, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin_1, axis)

origin_2 = Frame((cyl_length / 2, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin_2, axis)

origin_3 = Frame((cone_length + radius, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link3, link4, origin_3, axis)


# Create a configuration object matching the number of joints in your model
config = model.zero_configuration()

# Update the model using the artist
artist = Artist(model)

# Render everything
artist.draw_visual()
artist.redraw()

R = artist.draw_visual()

# Animate
for i in range(L):
    rotation = 0.1

    config['joint1'] = math.radians(i * rotation)
    config['joint2'] = math.radians(i * rotation)
    config['joint3'] = math.radians(i * rotation)
    config['joint4'] = math.radians(i * rotation)

    artist.update(config)
    R = artist.draw_visual()
