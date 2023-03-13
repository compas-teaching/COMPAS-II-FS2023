import math

from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection
from compas.geometry import Vector

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([1, 1, 1], [1, 1, 0], [0, 1, 1])

# Create a Box with that frame
box = Box(frame, 1, 1, 1)

# Create a Projection (can be orthogonal, parallel or perspective)
P  = Projection.from_plane_and_direction(Plane.worldXY(), Vector(math.sin(a)*math.cos(b), math.sin(a)*math.sin(b),math.cos(a)))

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)
# outTemp = mesh_projected

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw and all to a list
x = artist1.draw()
y = artist2.draw_edges(color="#00ff00")

