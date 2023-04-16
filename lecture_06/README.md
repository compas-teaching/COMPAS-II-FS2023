# COMPAS II: Assembly of discrete elements I

Pick'n'place planning.

Brief introduction to graphs.

Modelling assembly processes as DAGs.

👉 [Slides](https://docs.google.com/presentation/d/1UKz9m9L74iOrjT9Vg3ovRnctEWxSR5qnNkONd6xBSk4/edit?usp=sharing)

## Examples

Make sure you start (`compose up`) the container for the planning examples.

* Pick and Place planning with MoveIt
  * [Cartesian motion planning](309_plan_cartesian_motion_ros.py)
  * [Cartesian motion planning: visualization](310_plan_cartesian_motion_ros_artist.py)
  * [Free space motion planning](311_plan_motion_ros.py)
  * [Free space motion planning: visualization](312_plan_motion_ros_artist.py)
  * [Add objects to the scene](315_add_collision_mesh.py)
  * [Append nested objects to the scene](316_append_collision_meshes.py)
  * [Remove objects from the scene](317_remove_collision_mesh.py)
  * [Attach tool](400_attach_tool.py)
  * [Detach tool](401_detach_tool.py)

* Graphs
  * [Linear order](521_linear_order.py)
  * [Color-mixing lattice](522_color_mixing_lattice.py)
  * [Color-mixing lattice: visualization](523_color_mixing_lattice_artist.py)
  * [Partial order](524_partial_order.py)
  * [Network concepts](525_network_concepts.py)
  * [Using NetworkX](526_networkx.py)
