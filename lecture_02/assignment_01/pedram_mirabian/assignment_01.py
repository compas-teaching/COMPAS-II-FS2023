from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame, which is not in the origin and a bit tilted to the world frame
point_1 = (1, 3, 5)
xaxis_1 = (0.916893, 0, -0.399133)
yaxis_1 = (-0.04001, 0.994963, -0.091911)

frame = Frame(point_1, xaxis_1, yaxis_1)

# Create a Box with that frame
box = Box(frame, 1, 1.62, 2.62)

# Create a Projection (can be orthogonal, parallel or perspective)
plane = Plane.worldXY()
center_of_projection = [0, 0, 8]
P = Projection.from_plane_and_point(plane, center_of_projection)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw and all to a list
a1 = artist1.draw()
a2 = artist2.draw_edges(color="#00ff00")