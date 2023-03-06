"""Assignment 01: Project box to xy-plane
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([12, 33, 61], [-.3, 1, .6], [0.5, 0.3, 1])

# Dimension variables of the box
xsize = 12
ysize = 33
zsize = 61

# Create a Box with that frame
box = Box(frame, xsize, ysize, zsize)

# Create a Projection (can be orthogonal, parallel or perspective)
P = Projection.from_plane(Plane.worldXY())

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw and all to a list
artist1.draw()
artist2.draw_edges(color="#00ff00")
