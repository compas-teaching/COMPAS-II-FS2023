from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Line
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Cone
from compas.geometry import Capsule
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Translation
from compas.robots import Joint
from compas.robots import RobotModel

height = 0.5
length = 5
radiusBase, radiusColumn, radiusHead, radiusEye = 1.75, 0.25, 0.75, 3

# create cylinder and cone in xy plane
circle = Circle(Plane.worldXY(), radiusBase)
cylinder = Cylinder(circle, height)
cylinder.transform(Translation.from_vector([0, 0, height/2]))
cone01 = Cone(circle, height)
cone01.transform(Translation.from_vector([0, 0, height]))

cylinder01 = Cylinder(Circle(Plane.worldXY(), radiusColumn), length)
cylinder01.transform(Translation.from_vector([0, 0, length / 2]))

# create capsule and cone in xz plane
line = Line((0, radiusHead, 0), (0, 0, 0))
capsule01 = Capsule(line, radiusHead)
capsule01.transform(Translation.from_vector([0, 0, height]))
capsule01.transform(Translation.from_vector([0, -radiusHead/2, 0]))

plane = Plane([0, 0.85 * radiusEye, 0], [0, -1, 0])
circle = Circle(plane, 3)
cone02 = Cone(circle, radiusEye)
cone02.transform(Translation.from_vector([0, 0, height]))

# create robot model
model = RobotModel("luxo_jr", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh1 = Mesh.from_shape(cylinder)
mesh2 = Mesh.from_shape(cone01)
mesh3 = Mesh.from_shape(cylinder01)
mesh4 = Mesh.from_shape(cylinder01)
mesh5 = Mesh.from_shape(capsule01)
mesh6 = Mesh.from_shape(cone02)

mesh1.join(mesh2)
mesh5.join(mesh6)

# add links
world_link = model.add_link("world")
base_link = model.add_link("base_link", visual_mesh=mesh1, visual_color=(0.26, 0.34, 0.42))
lower_link = model.add_link("lower_link", visual_mesh=mesh3, visual_color=(0.58, 0.75, 0.92))
upper_link = model.add_link("upper_link", visual_mesh=mesh4, visual_color=(0.31, 0.62, 0.93))
head_link = model.add_link("head", visual_mesh=mesh5, visual_color=(0.45, 0.59, 0.72))

# add joints between the links
axis_y = (0, 1, 0)
axis_z = (0, 0, 1)

origin = Frame.worldXY()
model.add_joint("world_joint", Joint.PRISMATIC , world_link, base_link, origin, axis_z, [0 , 5])

origin.point.z = height*2
model.add_joint("base_joint", Joint.REVOLUTE, base_link, lower_link, origin, axis_y, [-3.14/2 , 3.14/2])

origin.point.z = length
model.add_joint("elbow_joint", Joint.REVOLUTE, lower_link, upper_link, origin, axis_y, [-3.14 , 3.14])

model.add_joint("head_joint", Joint.CONTINUOUS, upper_link, head_link, origin, axis_z)

# Create a configuration object matching the number of joints in your model
configuration = model.zero_configuration()
configuration.joint_values = [3.6, 1.2, -2.4, 0.6]

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

# Render everything
artist.draw_visual()
artist.redraw()

# Animate the bounce of Luxo_Jr
time = 120
# in Grasshopper we can skip  the above line and use a variable named time connected with a slider
# configuration.joint_values = [x, y, z, math.pi / 2 - y]
i = 0
direction = 1
for t in range(time):
    param = i / 25
    configuration["world_joint"] = abs(param) * 3
    configuration["base_joint"] = param
    configuration["elbow_joint"] = -2 * param
    configuration["head_joint"] = 0.5 * param
    if abs(i) == 30:
        direction = -direction
    i += direction
artist.update(configuration)
artist.draw_visual()
# for visualize it in Grasshopper
# a = artist.draw_visual()
artist.redraw()
