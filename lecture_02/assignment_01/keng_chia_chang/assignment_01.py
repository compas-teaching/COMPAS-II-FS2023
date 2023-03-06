"""Assignment 01: Project box to xy-plane
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([1, 0, 5], [-0.45, 0.1, 0.3], [1, 0, 0])

# Create a Box with that frame
box = box = Box(frame, 2, 2, 2)

# Create a Projection (can be orthogonal, parallel or perspective)
point, normal = [0, 0, 0], [0, 0, 1]
perspective = [10, 10, 10]
P = Projection.from_plane_and_point((point, normal), perspective)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
Mesh.transform(mesh, P)
print(P)
print(mesh)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh)

# Draw and all to a list
artist1.draw()
artist2.draw_edges(color="#00ff00")

a=mesh
b=box