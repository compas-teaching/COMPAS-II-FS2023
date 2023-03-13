

#[06|03|23] Assignment 01 // Nijat Mahamaliyev
#Assignment 01: Project box to xy-plane
""""
    Objective and steps:
        * Create a box at a certain location with a certain orientation.
        * Create a Projection (can be orthogonal, parallel or perspective)
        * Convert the box to a mesh and project the it onto the xy-plane.
        * Use artists to draw the result
"""


from compas.geometry import Quaternion
from compas.geometry import Rotation
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection


# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame =Frame.from_points([0, 10, 20], [20, 40, 60], [10, 30, 50])


#temp val
    #x=0.00, y=0.01, z=-0.60
    
# Create a Box with that frame
box = Box(frame, 7, 7, 7)
quaternion = Quaternion(w, x, y, z).unitized()
R = Rotation.from_quaternion(quaternion)
box=box.transformed(R)




P = Projection.from_plane_and_point(Plane.worldXY(), [0, 0, 10])

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw and all to a list
artist1.draw()
artist2.draw()
mesh_projected_edges = artist2.draw_edges(color="#00008B")