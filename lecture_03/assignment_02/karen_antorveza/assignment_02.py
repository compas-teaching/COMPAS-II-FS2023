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
from compas.geometry import Sphere
from compas.geometry import Point


# create cylinder in yz plane
radius, length = 0.3, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2.0, 0, 0]))

#body
radius1, length1 = 0.5, 3.5
cylinder1 = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius1), length1)
cylinder1.transform(Translation.from_vector([length1 / 2.0, 0, 0]))

#head
sphere1 = Sphere(Point(-1, 0, 0), 1)


# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh1 = Mesh.from_shape(cylinder)
mesh2 = Mesh.from_shape(cylinder1)
#mesh3 = Mesh.from_shape(cylinder)
#mesh4 = Mesh.from_shape(cylinder)
#mesh5 = Mesh.from_shape(cylinder)
mesh6 = Mesh.from_shape(sphere1)

# add links
link0 = model.add_link("world")
link1 = model.add_link("link1", visual_mesh=mesh1, visual_color=(0.78, 0.96, 0.30))
link2 = model.add_link("link2", visual_mesh=mesh1, visual_color=(0.78, 0.96, 0.30))
link3 = model.add_link("link3", visual_mesh=mesh2, visual_color=(0.78, 0.96, 0.33))
link4 = model.add_link("link4", visual_mesh=mesh1, visual_color=(0.3, 0.2, 0.8))
link5 = model.add_link("link5", visual_mesh=mesh1, visual_color=(0.3, 0.2, 0.8))
link6 = model.add_link("link6", visual_mesh=mesh6, visual_color=(0.78, 0.47, 0.15))

# add joints between the links
axis = (0, 0, 1)

origin1 = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin1, axis)

origin2 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin2, axis)

origin3 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link1, link3, origin3, axis)

origin4 = Frame((length1, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link3, link4, origin4, axis)

origin5 = Frame((length1, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint5", Joint.CONTINUOUS, link3, link5, origin5, axis)

origin6 = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint6", Joint.CONTINUOUS, link3, link6, origin1, axis)

# Create a configuration object matching the number of joints in your model
configuration = model.zero_configuration() #close to all zeros 
configuration.joint_values =[a, b, c, d, e, f]

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

# Render everything
artist.draw_visual()
artist.redraw()

geo = artist.draw_visual()
print(model)
