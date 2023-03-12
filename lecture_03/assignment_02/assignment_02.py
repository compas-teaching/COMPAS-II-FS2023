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

from compas.geometry import Plane
from compas.geometry import Cone
from compas.geometry import Scale
from compas.geometry import Line
from compas.geometry import Capsule

# create cylinder in yz plane
x, y, z = 0, 0, 0
height = 0.5
length = 5
radiusBase, radiusColumn, radiusHead, radiusEye = 1.75, 0.25, 0.75, 3

circle = Circle(Plane.worldXY(), radiusBase)
cylinder00 = Cylinder(circle, height)
cylinder00.transform(Translation.from_vector([0, 0, height/2]))
cone01 = Cone(circle, height)
cone01.transform(Translation.from_vector([0, 0, height]))

cylinder01 = Cylinder(Circle(Plane.worldXY(), radiusColumn), length)
cylinder01.transform(Translation.from_vector([0, 0, length / 2]))

line = Line((0, radiusHead, 0), (0, 0, 0))
capsule01 = Capsule(line, radiusHead)
capsule01.transform(Translation.from_vector([0, 0, height]))

plane = Plane([0, -1 * radiusEye, 0], [0, 1, 0])
circle = Circle(plane, 3)
cone02 = Cone(circle, radiusEye)
cone02.transform(Translation.from_vector([0, 0, height]))


# create robot model
model = RobotModel("luxo_jr", links=[], joints=[])



# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh1 = Mesh.from_shape(cylinder00)
mesh2 = Mesh.from_shape(cone01)
mesh3 = Mesh.from_shape(cylinder01)
mesh4 = Mesh.from_shape(cylinder01)
mesh5 = Mesh.from_shape(capsule01)
mesh6 = Mesh.from_shape(cone02)

mesh1.join(mesh2)
mesh5.join(mesh6)


# add links
world_link = model.add_link("world")
base_link = model.add_link("base", visual_mesh=mesh1, visual_color=(0.2, 0.5, 0.6)) # BLUE
lower_link = model.add_link("lower", visual_mesh=mesh3, visual_color=(0.5, 0.6, 0.2)) # GREEN
upper_link = model.add_link("upper", visual_mesh=mesh4, visual_color=(0.5, 0.6, 0.2)) # RED
head_link = model.add_link("head", visual_mesh=mesh5, visual_color=(0.5, 0.5, 0.5)) # BLACK

# add joints between the links
axis01 = (0, 1, 0)
axis02 = (0, 0, 1)

origin = Frame((x, y, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint1", Joint.PRISMATIC , world_link, base_link, origin, axis02, [0 , 5])

origin = Frame((x, y, height*2), (0, -1, 0), (1, 0, 0))
model.add_joint("joint2", Joint.REVOLUTE, base_link, lower_link, origin, axis01, [-3.14 , 3.14])

origin = Frame((x, y, length), (0, -1, 0), (1, 0, 0))
model.add_joint("joint3", Joint.REVOLUTE, lower_link, upper_link, origin, axis01*(-1), [-3.14 , 3.14])

origin = Frame((x, y, length), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, upper_link, head_link, origin, axis02)

# Create a configuration object matching the number of joints in your model
# configuration = ....
# https://compas.dev/compas/latest/api/generated/compas.robots.Configuration.html?highlight=configuration#compas.robots.Configuration
configuration = model.zero_configuration()
configuration.joint_values = [0, -0.47, -1.57, -0.66]

# Update the model using the artist
artist = Artist(model)

# artist.update ...
artist.update(configuration)

# Render everything
artist.draw_visual()
A = artist.draw_visual()
artist.redraw()

##################################################
"""
BOUNCING IN GH

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

from compas.geometry import Plane
from compas.geometry import Cone
from compas.geometry import Scale
from compas.geometry import Line
from compas.geometry import Capsule

# create cylinder in yz plane
x, y, z = 0, 0, 0
height = 0.5
length = 5
radiusBase, radiusColumn, radiusHead, radiusEye = 1.75, 0.25, 0.75, 3

circle = Circle(Plane.worldXY(), radiusBase)
cylinder00 = Cylinder(circle, height)
cylinder00.transform(Translation.from_vector([0, 0, height/2]))
cone01 = Cone(circle, height)
cone01.transform(Translation.from_vector([0, 0, height]))

cylinder01 = Cylinder(Circle(Plane.worldXY(), radiusColumn), length)
cylinder01.transform(Translation.from_vector([0, 0, length / 2]))

line = Line((0, radiusHead, 0), (0, 0, 0))
capsule01 = Capsule(line, radiusHead)
capsule01.transform(Translation.from_vector([0, 0, height]))

plane = Plane([0, -1 * radiusEye, 0], [0, 1, 0])
circle = Circle(plane, 3)
cone02 = Cone(circle, radiusEye)
cone02.transform(Translation.from_vector([0, 0, height]))


# create robot model
model = RobotModel("luxo_jr", links=[], joints=[])



# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh1 = Mesh.from_shape(cylinder00)
mesh2 = Mesh.from_shape(cone01)
mesh3 = Mesh.from_shape(cylinder01)
mesh4 = Mesh.from_shape(cylinder01)
mesh5 = Mesh.from_shape(capsule01)
mesh6 = Mesh.from_shape(cone02)

mesh1.join(mesh2)
mesh5.join(mesh6)


# add links
world_link = model.add_link("world")
base_link = model.add_link("base", visual_mesh=mesh1, visual_color=(0.2, 0.5, 0.6)) # BLUE
lower_link = model.add_link("lower", visual_mesh=mesh3, visual_color=(0.5, 0.6, 0.2)) # GREEN
upper_link = model.add_link("upper", visual_mesh=mesh4, visual_color=(0.5, 0.6, 0.2)) # RED
head_link = model.add_link("head", visual_mesh=mesh5, visual_color=(0.5, 0.5, 0.5)) # BLACK

# add joints between the links
axis01 = (0, 1, 0)
axis02 = (0, 0, 1)

origin = Frame((x, y, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint1", Joint.PRISMATIC , world_link, base_link, origin, axis02, [0 , 5])

origin = Frame((x, y, height*2), (0, -1, 0), (1, 0, 0))
model.add_joint("joint2", Joint.REVOLUTE, base_link, lower_link, origin, axis01, [-3.14/2 , 3.14/2])

origin = Frame((x, y, length), (0, -1, 0), (1, 0, 0))
model.add_joint("joint3", Joint.REVOLUTE, lower_link, upper_link, origin, axis01*(-1), [-3.14 , 3.14])

origin = Frame((x, y, length), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, upper_link, head_link, origin, axis02)

# Create a configuration object matching the number of joints in your model
# configuration = ....
# https://compas.dev/compas/latest/api/generated/compas.robots.Configuration.html?highlight=configuration#compas.robots.Configuration
configuration = model.zero_configuration()
configuration.joint_values = [a, b, 2*b, d]

# Update the model using the artist
artist = Artist(model)

# artist.update ...
artist.update(configuration)

# Render everything
artist.draw_visual()
A = artist.draw_visual()
artist.redraw()
"""