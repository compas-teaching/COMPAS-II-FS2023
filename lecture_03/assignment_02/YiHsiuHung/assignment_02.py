from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Circle,Cylinder,Box,Sphere,Polygon
from compas.geometry import boolean_union_mesh_mesh
from compas.geometry import trimesh_remesh

from compas.geometry import Frame,Plane
from compas.geometry import Translation
from compas.robots import Configuration
from compas.robots import Joint
from compas.robots import RobotModel

# create cylinder in yz plane
radius, length = 2, 2
hand_length = 5
hand_length_02 = 3

xaxis = [1, 0, 0]
yaxis = [0, 1, 0]
frame = Frame([0,0,0], xaxis, yaxis)
box_body = Box(frame, 10, 10, 10)
frame_right = Frame([6,0,-2], xaxis, yaxis)
right_hand = Box(frame_right, 2, 2, hand_length)
frame_left = Frame([-6,0,-2], xaxis, yaxis)
left_hand = Box(frame_left, 2, 2, hand_length)
frame_right_02 = Frame([6,0,-2], xaxis, yaxis)
right_hand_02 = Box(frame_right_02, 1, 1, hand_length_02)
frame_left_02 = Frame([-6,0,-2], xaxis, yaxis)
left_hand_02 = Box(frame_left_02, 1, 1, hand_length_02)


neck_down = Box(Frame([0,0,2], xaxis, yaxis), 2, 1, 5)
neck_up = Box(frame, 2, 1, 3)
eye_right = Cylinder(Circle(Plane([0, 0, 0], [0, 1, 0]), radius), length)
eye_left = Cylinder(Circle(Plane([0, 0, 0], [0, 1, 0]), radius), length)
eye_right_in = Cylinder(Circle(Plane([0, 0, 0.5], [0, 1, 0]), 1), 1)
eye_left_in = Cylinder(Circle(Plane([0, 0, 0.5], [0, 1, 0]), 1), 1)

# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh1 = Mesh.from_shape(box_body)
mesh2 = Mesh.from_shape(right_hand)
mesh3 = Mesh.from_shape(left_hand)
mesh4 = Mesh.from_shape(right_hand_02)
mesh5 = Mesh.from_shape(left_hand_02)
mesh6 = Mesh.from_shape(neck_down)
mesh7 = Mesh.from_shape(neck_up)
mesh8 = Mesh.from_shape(eye_right)
mesh9 = Mesh.from_shape(eye_left)
mesh10 = Mesh.from_shape(eye_right_in)
mesh11 = Mesh.from_shape(eye_left_in)


# add links
link0 = model.add_link("world")
link1 = model.add_link("link1", visual_mesh=mesh1, visual_color=(0.2, 0.5, 0.6))
link2 = model.add_link("link2", visual_mesh=mesh2, visual_color=(0.5, 0.6, 0.2))
link3 = model.add_link("link3", visual_mesh=mesh3, visual_color=(0.5, 0.6, 0.2))
link4 = model.add_link("link4", visual_mesh=mesh4, visual_color=(0.5, 0.1, 0.2))
link5 = model.add_link("link5", visual_mesh=mesh5, visual_color=(0.5, 0.1, 0.2))
link6 = model.add_link("link6", visual_mesh=mesh6, visual_color=(0.2, 0.2, 0.2))
link7 = model.add_link("link7", visual_mesh=mesh7, visual_color=(0.2, 0.2, 0.2))
link8 = model.add_link("link8", visual_mesh=mesh8, visual_color=(0.8, 0.8, 0.8))
link9 = model.add_link("link9", visual_mesh=mesh9, visual_color=(0.8, 0.8, 0.8))
link10 = model.add_link("link10", visual_mesh=mesh10, visual_color=(0.1, 0.1, 0.1))
link11 = model.add_link("link11", visual_mesh=mesh11, visual_color=(0.1, 0.1, 0.1))

# add joints between the links
Xaxis = (1, 0, 0)
Yaxis = (0, 1, 0)
Zaxis = (0, 0, 1)

origin1 = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin1, Zaxis)

origin2 = Frame((0, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, Frame([0,0,4], xaxis, yaxis), Xaxis)
model.add_joint("joint3", Joint.CONTINUOUS, link1, link3, Frame([0,0,4], xaxis, yaxis), Xaxis)
model.add_joint("joint4", Joint.REVOLUTE, link1, link6, Frame([0,0,4], xaxis, yaxis), Xaxis, [-3.14/3 , 3.14/3])

model.add_joint("joint5", Joint.REVOLUTE, link2, link4, Frame([0,0,-4], xaxis, yaxis), Xaxis, [-3.14/2 , 3.14/2])
model.add_joint("joint6", Joint.REVOLUTE, link3, link5, Frame([0,0,-4], xaxis, yaxis), Xaxis, [-3.14/2 , 3.14/2])

model.add_joint("joint7", Joint.REVOLUTE, link6, link7,Frame([0,0,5], xaxis, yaxis), Xaxis, [-3.14/4 , 3.14/4])
model.add_joint("joint8", Joint.CONTINUOUS, link7, link8,Frame([2.5,0,0], xaxis, yaxis), Yaxis)
model.add_joint("joint9", Joint.CONTINUOUS, link7, link9,Frame([-2.5,0,0], xaxis, yaxis), Yaxis)

model.add_joint("joint10", Joint.CONTINUOUS, link8, link10,Frame([0,-1,0], xaxis, yaxis), Yaxis)
model.add_joint("joint11", Joint.CONTINUOUS, link9, link11,Frame([0,-1,0], xaxis, yaxis), Yaxis)

# Create a configuration object matching the number of joints in your model
configuration = model.zero_configuration()
configuration.joint_values = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] 


# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

# Render everything
artist.draw_visual()
artist.redraw()

# for visualize it in Grasshopper
# a = artist.draw_visual()