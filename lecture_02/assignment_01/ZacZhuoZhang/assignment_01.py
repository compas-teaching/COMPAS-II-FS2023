from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection
from compas.geometry import Vector
import math

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([1, 1, 1], [1, 1, 0], [0,1, 1])

# Create a Box with that frame
box = Box(frame, 1, 1, 1)
outTemp = box

# Create a Projection (can be orthogonal, parallel or perspective)
P  = Projection.from_plane_and_direction(Plane.worldXY(), Vector(math.sin(θ)*math.cos(φ), math.sin(θ)*math.sin(φ),math.cos(θ)))

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)
# outTemp = mesh_projected

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw and all to a list
# artist1.draw()
# artist2.draw_edges(color="#00ff00")
