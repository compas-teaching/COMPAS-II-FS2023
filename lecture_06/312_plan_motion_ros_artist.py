import math
import time

from compas.artists import Artist
from compas.geometry import Frame
from compas_fab.backends import RosClient

with RosClient("localhost") as client:
    robot = client.load_robot(load_geometry=True)
    group = robot.main_group_name

    frame = Frame((-0.3, 0.3, 0.05), (0, 1, 0), (1, 0, 0))
    tolerance_position = 0.001
    tolerance_axes = [math.radians(1)] * 3

    start_configuration = robot.zero_configuration()
    start_configuration.joint_values = (0.644, 0.674, 0.826, 0.000, 0.071, 2.214)

    # create goal constraints from frame
    goal_constraints = robot.constraints_from_frame(frame, tolerance_position, tolerance_axes, group)

    trajectory = robot.plan_motion(goal_constraints, start_configuration, group, options=dict(planner_id="RRT"))

    print("Computed free-space path with %d configurations." % len(trajectory.points))
    print("Executing this path at full speed would take approx. %.3f seconds." % trajectory.time_from_start)

    artist = Artist(robot.model, layer="Robot")

    for tp in trajectory.points:
        config = robot.zero_configuration()
        config.joint_values = tp.joint_values
        artist.update(config)
        artist.clear_layer()
        artist.draw_visual()
        artist.redraw()
        time.sleep(0.01)
