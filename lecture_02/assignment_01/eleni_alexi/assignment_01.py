"""Assignment 01: Project box to xy-plane
"""
from compas.artists import Artist
from compas.artists import MeshArtist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([10, 4, 8], [1, -0.75, 0], [0, 0.25, -0.2])

# Create a Box with that frame
box = Box(frame, 4, 3, 5)

# Create a perspective Projection Transformation to project onto the xy-plane from a single point
P = Projection.from_plane_and_point(Plane.worldXY(), [5, 3, 2])

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = Artist(box)
artist2 = MeshArtist(mesh_projected)

# Draw all and add to a list
a = [artist1.draw()]
a.extend(artist2.draw_edges(color="#00ff00"))
