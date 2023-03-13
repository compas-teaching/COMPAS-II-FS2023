"""Assignment 01: Project box to xy-plane
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection
from compas.geometry import Point
from compas.geometry import Vector

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame(Point(1, 3, 1), Vector(1, 0, -1.0), Vector(-0.5, 1, 0))

# Create a Box with that frame
box = Box(frame, 4, 4, 4)

# Create a Projection (can be orthogonal, parallel or perspective)
plane = Plane([0, 0, 0], [0, 0, 1])
P = Projection.from_plane(plane)

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
