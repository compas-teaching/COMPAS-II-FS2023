# COMPAS II: Path planning with ROS & MoveIt in the design environment

Robot planning: forward and inverse kinematic functions, cartesian and free-space planning. 
Planning scene operations. End effectors and discrete build elements.

Introduction to ROS, topics, services, actions. Basic interprocess communication via ROS nodes.

👉 [Slides](https://docs.google.com/presentation/d/1yL4ZTd4Xg-LmVAMjIti9pSgF-qUkO6B839qIuSsXe_A/edit?usp=sharing)

## Examples

* ROS & MoveIt planning
  * [Load robot](305_robot_from_ros.py)
  * [Load robot: visualization](306_robot_from_ros_artist.py)
  * [Forward Kinematics](307_forward_kinematics_ros.py)
  * [Inverse Kinematics](308_inverse_kinematics_ros.py)
  * [Cartesian motion planning](309_plan_cartesian_motion_ros.py)
  * [Cartesian motion planning: visualization](310_plan_cartesian_motion_ros_artist.py)
  * [Free space motion planning](311_plan_motion_ros.py)
  * [Free space motion planning: visualization](312_plan_motion_ros_artist.py)
  * [Constraints](313_constraints.py)

* Planning scene in MoveIt
  * [Planning scene preview in GH](314_planning_scene.ghx)
  * [Add objects to the scene](315_add_collision_mesh.py)
  * [Append nested objects to the scene](316_append_collision_meshes.py)
  * [Remove objects from the scene](317_remove_collision_mesh.py)

* ROS Concepts
  * [Verify connection](331_check_connection.py)
  * [Interconnected nodes: Listener](332_ros_hello_world_listener.py)
  * [Interconnected nodes: Talker](333_ros_hello_world_talker.py)
  * [Interconnected nodes: Talker in GH](334_ros_hello_world_talker.ghx)
