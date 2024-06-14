from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection
from compas.geometry import Point
from compas.geometry import Vector

point = Point(5.00, 5.00, 10.00)
xaxis = Vector(1.0000, 0.0000, 0.000)
yaxis = Vector(0.0000, 1.0000, 3.000)
frame = Frame(point,xaxis,yaxis)

box = Box(frame,5.0,5.0,5.0)

point, normal = [0, 0, 0], [0, 0, 1]
perspective = [0, 5, 5]
P = Projection.from_plane_and_point((point, normal), perspective)

mesh = Mesh.from_shape(box)
mesh.transform(P)


a = mesh
b = box

artist1 = Artist(b)
artist2 = Artist(a)

artist1.draw()
artist2.draw_edges(color="#00ff00")