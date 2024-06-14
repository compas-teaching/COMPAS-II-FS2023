"""Assignment 01: Project box to xy-plane
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([20, 0, 10], [-0.45, 0.1, 0.3], [1, 0, 0])
plane = Plane([0,0,0],[0,0,1])
direction = [-0.45,0,-1]
perspective = [6,8,20]

# Create a Box with that frame
w, l, h = 5, 5, 8
box = Box(frame, w, l, h)

# Create a Projection (can be orthogonal, parallel or perspective)
P_orthogonal = Projection.from_plane(plane)
P_parallel = Projection.from_plane_and_direction(plane, direction)
P_perspective = Projection.from_plane_and_point(plane, perspective)
# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P_perspective)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw and all to a list
a = artist1.draw()
b = artist2.draw_edges(color="#00ff00")
#a = [artist1.draw(), artist2.draw()]
