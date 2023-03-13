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
from compas.geometry import Point
from compas.geometry import Vector

# create pirmitives
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
c1 = cylinder.transformed(Translation.from_vector([length/2, y, 0.0]))
c2 = cylinder.transformed(Translation.from_vector([length/2, -y, 0.0]))
c3 = cylinder.transformed(Translation.from_vector([-length/2, y, 0.0]))
c4 = cylinder.transformed(Translation.from_vector([-length/2, -y, 0.0]))
box = Box(Frame.worldXY(),8.0,10.0,2.0)

# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh1 = Mesh.from_shape(box)
mesh2 = Mesh.from_shape(c1)
mesh3 = Mesh.from_shape(c2)
mesh4 = Mesh.from_shape(c3)
mesh5 = Mesh.from_shape(c4)

# add links
link0 = model.add_link("world")
link1 = model.add_link("link1", visual_mesh=mesh1, visual_color=(0.2, 0.5, 0.6))
link2 = model.add_link("link2", visual_mesh=mesh2, visual_color=(0.5, 0.6, 0.2))
link3 = model.add_link("link3", visual_mesh=mesh3, visual_color=(0.5, 0.6, 0.2))
link4 = model.add_link("link4", visual_mesh=mesh4, visual_color=(0.5, 0.6, 0.2))
link5 = model.add_link("link5", visual_mesh=mesh5, visual_color=(0.5, 0.6, 0.2))

# add joints between the links
axis1 = (0, 1, 0)
axis2 = (0, 0, 1)

origin1 = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin1, axis2)

origin2 = Frame((x/2, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin2, axis1)

origin3 = Frame((x/2, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link1, link3, origin3, axis1)

origin4 = Frame((-x/2, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link1, link4, origin4, axis1)

origin5 = Frame((-x/2, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint5", Joint.CONTINUOUS, link1, link5, origin5, axis1)

# Create a configuration object matching the number of joints in your model
configuration = model.zero_configuration()
configuration.joint_values = [rx,ry,rz,rc,rb]
#model.update(configuration)

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

# Render everything
result = artist.draw_visual()
artist.redraw()