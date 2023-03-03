"""Assignment 01: Project box to xy-plane
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame, which is not in the origin and a bit tilted to the world frame
# frame =
frame = Frame([1, 1, 0], [0.5, 0, 0.5], [1, 1, 0])

# Create a Box with that frame
# box = ...
box = Box(frame, 10, 5, 5)

# Create a Projection (can be orthogonal, parallel or perspective)
# P = Projection.from_...
plane = Plane([1, 1, 0], [0, 0, -1])
P = Projection.from_plane(plane)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
# mesh_projected = ...
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw and all to a list
artist1.draw()
artist2.draw_edges(color="#00ff00")
p=plane.worldXY