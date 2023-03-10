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
from compas.geometry import Cone
from compas.geometry import Sphere

# create cylinder in yz plane

length = 5
frame = Frame([0,0,0],[0,1,0],[0,0,1])
circle = Circle(Plane.from_frame(frame), 0.09)
point = (0,0,0)
cylinder_length = 1
cone_length = 0.3
sphere_radius = 0.7
box_x, box_y, box_z = 0.1, 0.15, 0.2

cylinder = Cylinder(circle, cylinder_length)
box = Box(frame, box_x,box_y,box_z)
cone = Cone(circle, cone_length)
sphere = Sphere(point, sphere_radius)

# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)

mesh1 = Mesh.from_shape(box)
mesh2 = Mesh.from_shape(cylinder)
mesh3 = Mesh.from_shape(cone)
mesh4 = Mesh.from_shape(sphere)

# add links
link0 = model.add_link("world")
link1 = model.add_link("link1", visual_mesh=mesh1, visual_color=(0.2, 0.5, 0.6))
link2 = model.add_link("link2", visual_mesh=mesh2, visual_color=(0.5, 0.6, 0.2))
link3 = model.add_link("link3", visual_mesh=mesh3, visual_color=(0.1, 0.4, 0.9))
link4 = model.add_link("link4", visual_mesh=mesh4, visual_color=(0.3, 0.2, 0.1))

# add joints between the links
axis = (0, 0, 1)

origin = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin, axis)

origin = Frame((box_x + cylinder_length/2 , 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin, axis)

origin = Frame((cylinder_length/2, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin, axis)

origin = Frame((sphere_radius + cone_length  , 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link3, link4, origin, axis)


# Create a configuration object matching the number of joints in your model
configuration = model.zero_configuration()

# Update the model using the artist
artist = Artist(model)
# artist.update ...

# Render everything
artist.draw_visual()
artist.redraw()
