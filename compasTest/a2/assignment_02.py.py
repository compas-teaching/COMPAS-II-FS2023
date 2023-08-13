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
from math import pi
import copy as co
import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th

freq = [(x-y)*iAmp for x, y in zip(iFreq[:], iFreq[1:])]
print(len(freq))

# create cylinder in yz plane
radius = iR
length = 5

dict_cylinder = {}
for i, r in enumerate(iR):
    dict_cylinder[i] = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), r), length)
    dict_cylinder[i].transform(Translation.from_vector([length / 2.0, 0, 0]))

# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
dict_mesh = {}
for i in range(len(iR)):
    dict_mesh[i] = Mesh.from_shape(dict_cylinder[i])

# add links
dict = {}
for i in range(len(iFreq)):
    if i == 0:
        dict[i] = model.add_link("world")
    else:
        dict[i] = model.add_link("link{}".format(i), visual_mesh=dict_mesh[i-1], visual_color=(1/len(iFreq)*i, 0.5, 0.6))


# add joints between the links
axis = (0, 0, 1)
axis1 = (0, 1, 0)

for i in range(len(freq)):
    if i == 0:
        origin = Frame.worldXY()
        model.add_joint("joint0", Joint.CONTINUOUS, dict[i], dict[i+1], origin, axis)
    else:
        origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
        model.add_joint("joint{}".format(i), Joint.CONTINUOUS, dict[i], dict[i+1], origin, axis)


# Create a configuration object matching the number of joints in your model
configuration = model.zero_configuration()
configuration.joint_values = freq

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

# Render everything
artist.draw_visual()
artist.redraw()
meshes = artist.draw_visual()

oMesh = []
for i in range(iNum):
    angle = 2*pi/iNum*i
    tran = rg.Transform.Rotation(angle, rg.Point3d(0,0,0))
    new = co.deepcopy(meshes)
    [mesh.Transform(tran) for mesh in new]
    oMesh.append(new)

oMesh = th.list_to_tree(oMesh)