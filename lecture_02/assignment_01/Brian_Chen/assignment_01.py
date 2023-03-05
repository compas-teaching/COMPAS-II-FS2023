
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Given: frame and box in the world coordinate system
frame = Frame([2, 2, 3], [0.978, 0.998, 0.610], [0.090, 0.452, 1.963])
width, length, height = 3, 2, 1
box = Box(frame, width, length, height)

# Construct an orthogonal projection transformation to project onto a plane
point = [0, 0, 0]
normal = [0, 0, 1]
plane = Plane(point, normal)
P = Projection.from_plane(plane)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# create artists
artist1 = Artist(mesh)
artist2 = Artist(mesh_projected)

# draw all and add to a list
a = [artist1.draw(), artist2.draw()]

"Question : Can not vistualize Mesh edges."
#a = [artist1.draw(), artist2.draw_edges(color="#00ff00")]