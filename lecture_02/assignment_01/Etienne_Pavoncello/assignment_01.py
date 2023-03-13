from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection
from compas.geometry import Point
from compas.geometry import Vector

point = Point(15, 15, 15)
xaxis = Vector(1, 0, 0)
yaxis = Vector(0, 1, 10)
frame = Frame(point,xaxis,yaxis)

box = Box(frame,10,10,10)

point, normal = [5, 5, 0], [10, 10, 10]
perspective = [10, 10, 5]
P = Projection.from_plane_and_point((point, normal), perspective)

mesh = Mesh.from_shape(box)
mesh_p = mesh.transformed(P)


a = mesh
b = mesh_p

artist1 = Artist(box)
artist2 = Artist(mesh_p)

artist1.draw()
artist2.draw_edges(color="#00ff00")