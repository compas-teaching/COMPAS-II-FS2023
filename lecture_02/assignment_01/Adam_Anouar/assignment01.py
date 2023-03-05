"""Assignment 01: Project box to xy-plane
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame with 3 points
frame = Frame.from_points([0, 3, 5], [3, 6, 9], [1, 0, 0])

# Create a Box with that frame
box = Box(frame, 2, 2, 2)

# Create a Projection (can be orthogonal, parallel or perspective)
P = Projection.from_plane_and_point(Plane([0, 2, 0], [0, 0, -1]), [0 ,0 ,-10])

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