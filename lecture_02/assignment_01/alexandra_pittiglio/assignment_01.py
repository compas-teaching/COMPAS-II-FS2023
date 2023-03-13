"""Assignment 01: Project box to xy-plane
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([1, 1, 0], [0, 0.25, -.25], [1, 0, 0])

# Create a Box with that frame
box = Box(frame, 3, 2, 1.5)

# Create a Projection (can be orthogonal, parallel or perspective)
P = Projection.from_plane(Plane.worldXY())

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transform(P)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh)

# Draw and all to a list
a = artist1.draw()
artist2.draw_edges(color="#00ff00")