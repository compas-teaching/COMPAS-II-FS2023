"""Assignment 01: Project box to xy-plane
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame_1 = Frame((1,3,2), (0.5,1,0), (1,0,0.5))

# Create a Box with that frame
box_1 = Box(frame_1, 2,3,4)

# Create a Projection (can be orthogonal, parallel or perspective)
# plane_1 = Projection.from_plane(Plane.worldXY())
plane_1 = Plane([0,0,0], [0,0,1])
P = Projection.from_plane_and_point(plane_1, (10,10,10))

# Create a Mesh from the Box
mesh = Mesh.from_shape(box_1)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = Artist(box_1)
artist2 = Artist(mesh_projected)

# Draw and all to a list
artist1.draw()
artist2.draw_edges(color="#00ff00")
