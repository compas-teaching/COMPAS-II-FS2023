# Assignment 01

Project box to xy-plane:

* Create a box at a certain location with a certain orientation.
* Create a Projection (can be orthogonal, parallel or perspective)
* Convert the box to a mesh and project the it onto the xy-plane.
* Use artists to draw the result

## How to start

Use the following code as a starting point for your assignment:

```python
"""Assignment 01: Project box to xy-plane
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

# Define a Frame, which is not in the origin and a bit tilted to the world frame
# frame =

# Create a Box with that frame
# box = ...

# Create a Projection (can be orthogonal, parallel or perspective)
# P = Projection.from_...

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
# mesh_projected = ...

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw and all to a list
artist1.draw()
artist2.draw_edges(color="#00ff00")