# Assignment submission Carl P-Conquilla for COMPASII FS2023
# Assignment 01: Project box to xy-plane


from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame.from_euler_angles([0, 0.6, 0.8])

# Create a Box with that frame
box = Box(frame, 10, 12, 16)

# Create a Projection (can be orthogonal, parallel or perspective)
P = Projection.from_plane(Plane.from_three_points(  [6, 9, 11], 
                                                    [17, -5, -7], 
                                                    [24, 14, -32]))

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