#   code intended for GhPython component with inputs: 
#   length(0,10), radius(0.0,1.0), geo_modifier(0.1,1.5), config(list<radians>), len = 5
#   hence the reportUndefinedVariable

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

length_1 = length
radius_1 = radius
cylinder_1 = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius_1), length_1)
cylinder_1.transform(Translation.from_vector([length_1 / 2.0, 0, 0]))

length_2 = length * geo_modifier
radius_2 = radius / geo_modifier
cylinder_2 = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius_2), length_2)
cylinder_2.transform(Translation.from_vector([length_2 / 2.0, 0, 0]))

# create robot model

model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)

mesh1 = Mesh.from_shape(cylinder_1)
mesh2 = Mesh.from_shape(cylinder_1)
mesh3 = Mesh.from_shape(cylinder_1)
mesh4 = Mesh.from_shape(cylinder_2)
mesh5 = Mesh.from_shape(cylinder_2)

# add links

link0 = model.add_link("link0")
link1 = model.add_link("link1", visual_mesh=mesh1, visual_color=(0.2, 0.5, 0.6))
link2 = model.add_link("link2", visual_mesh=mesh2, visual_color=(0.5, 0.6, 0.2))
link3 = model.add_link("link3", visual_mesh=mesh3, visual_color=(0.1, 0.4, 0.2))
link4 = model.add_link("link4", visual_mesh=mesh4, visual_color=(0.2, 0.6, 0.3))
link5 = model.add_link("link5", visual_mesh=mesh5, visual_color=(0.4, 0.2, 0.3))

# add joints between the links

axis = (0, 0, 1)

origin = Frame((0, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin, axis)

origin = Frame((length_1, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin, axis)

origin = Frame((length_1, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin, axis)

origin = Frame((length_1, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link3, link4, origin, axis)

origin = Frame((length_2, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint5", Joint.CONTINUOUS, link4, link5, origin, axis)


# Create a configuration object matching the number of joints in your model

configuration = model.zero_configuration()
configuration.joint_values = config

# Update the model using the artist

artist = Artist(model)
artist.update(configuration)

# Render everything

artist = artist.draw_visual()