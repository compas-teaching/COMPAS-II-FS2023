# Assignment 01

#Project box to xy-plane:
#
#* Create a box at a certain location with a certain orientation.
#* Create a Projection (can be orthogonal, parallel or perspective)
#* Convert the box to a mesh and project the it onto the xy-plane.
#* Use artists to draw the result

## How to start
#
#Use the following code as a starting point for your assignment:
#
#```python
"""Assignment 01: Project box to xy-plane
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame =Frame(Point(1, 5, 5), Vector(-0.45, 0.1, 0.3), Vector(1, 1, 0))
width, length, height = 3, 3, 3
# Create a Box with that frame
box = Box(frame, width, length, height)

# Create a Projection (can be orthogonal, parallel or perspective)
P = Projection.from_plane(Plane.worldXY())

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.copy()
Mesh.transform(mesh_projected,P)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh)
artist3 = Artist(mesh_projected)
# Draw and all to a list
artist1.draw()
artist2.draw_edges(color="#00ff00")

a= mesh
b= mesh_projected