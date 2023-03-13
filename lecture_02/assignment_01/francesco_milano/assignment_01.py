from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# construct a frame
frame = Frame([0, 0, 200], [0, 1, 0], [1, 0, 0])

#construct a box
width, length, height = 200, 100, 100
box = Box(frame, width, length, height)

# transformatin matrix
point = [0, 0, 0]
normal = [0, 0, 1]
plane = Plane(point, normal)
direction = [1, 1, 1]  #
P = Projection.from_plane_and_direction(plane, direction)

# box to mesh
mesh = Mesh.from_shape(box)

# apply the projection onto the mesh
mesh_projected = Mesh.transformed(mesh, P)
# why transformED?

# display
artist1 = Artist(box)
artist2 = Artist(mesh_projected)
artist1.draw()
artist2.draw_edges(color="#00ff00")
