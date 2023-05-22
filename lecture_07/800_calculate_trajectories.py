from compas.datastructures import Assembly
from compas.geometry import Frame
from compas.geometry import Plane
from compas_fab.backends import RosClient
from compas_fab.robots import Tool
from compas.datastructures import Mesh


import os
from helpers import generate_default_tolerances
from helpers import get_assembly_sequence

APPROACH_DISTANCE = 0.1
group = None
start_configuration = None


def calculate_pick_trajectory(pick_frame, robot):
    # Calculate pick trajectory
    approach_pick_frame = pick_frame.copy()
    approach_pick_frame.point.z += APPROACH_DISTANCE

    pick_config = robot.inverse_kinematics(pick_frame, start_configuration, group)
    approach_pick_config = robot.inverse_kinematics(approach_pick_frame, pick_config, group)

    max_step = 0.01
    frames = [
        robot.forward_kinematics(c, group, options=dict(solver="model")) for c in (approach_pick_config, pick_config)
    ]

    trajectory = robot.plan_cartesian_motion(
        frames,
        start_configuration=approach_pick_config,
        group=group,
        options=dict(
            max_step=max_step,
        ),
    )
    if trajectory.fraction < 1:
        raise Exception(
            "Incomplete cartesian trajectory found. Only {:.1f}% of the trajectory could be planned".format(
                trajectory.fraction * 100
            )
        )

    return trajectory, pick_config, approach_pick_config

HERE = os.path.dirname(__file__)

assembly = Assembly.from_json("lecture_07/assembly-data.json")
mesh = Mesh.from_stl(os.path.join(HERE, "vacuum_gripper.stl"))
tool = Tool(mesh, Frame([0, 0, 0.07], [1, 0, 0], [0, 1, 0]))
# tool = Tool.from_data(assembly.attributes["robot_tool"])
pick_frame = Frame.from_plane(Plane([0.78,0.01,0.01], [0.00,0.00,-1.00]))

# 0. O(0.78,0.01,0.01) Z(0.00,0.00,-1.00)
# pick_frame = Frame.from_data(assembly.attributes["pickup_frame"])

with RosClient() as ros:
    robot = ros.load_robot(load_geometry=False)
    robot.attach_tool(tool)

    print("Calculate pick trajectory")
    pick_trajectory, pick_config, approach_pick_config = calculate_pick_trajectory(pick_frame, robot)
    print("Calculate pick trajectory: done")

    top_course = assembly.attributes["courses"]
    sequence = get_assembly_sequence(assembly, top_course)

    i = 0
    for index in sequence:
        i += 1
        print(f"{i}. Calculate part key={sequence[index]} place trajectory")
        part = assembly.find_by_key(sequence[index])
        if "move_trajectory" in part.attributes:
            continue

        try:
            place_frame = part.attributes["place_frame"].copy()
            approach_place_frame = place_frame.copy()
            if APPROACH_DISTANCE > 0:
                approach_place_frame.point.z += APPROACH_DISTANCE

            place_config = robot.inverse_kinematics(place_frame, approach_pick_config, group)
            approach_place_config = robot.inverse_kinematics(approach_place_frame, place_config, group)

            # part.attributes["place_config"] = place_config
            # part.attributes["approach_place_config"] = approach_place_config

            max_step = 0.01
            frames = [
                robot.forward_kinematics(c, group, options=dict(solver="model"))
                for c in (approach_place_config, place_config)
            ]

            place_trajectory = robot.plan_cartesian_motion(
                frames,
                start_configuration=approach_place_config,
                group=group,
                options=dict(
                    max_step=max_step,
                ),
            )

            if place_trajectory.fraction < 1:
                raise Exception(
                    "Incomplete cartesian trajectory found. Only {:.1f}% of the trajectory could be planned".format(
                        place_trajectory.fraction * 100
                    )
                )

            tolerance_above = generate_default_tolerances(robot.get_configurable_joints(group))
            tolerance_below = generate_default_tolerances(robot.get_configurable_joints(group))
            goal_constraints = robot.constraints_from_configuration(
                configuration=approach_place_config,
                tolerances_above=tolerance_above,
                tolerances_below=tolerance_below,
                group=group,
            )

            move_trajectory = robot.plan_motion(
                goal_constraints,
                start_configuration=approach_pick_config,
                group=group,
                options=dict(
                    planner_id="BiTRRT",
                ),
            )

            # Save everything to part
            part.attributes["approach_pick_config"] = approach_pick_config
            part.attributes["pick_config"] = pick_config
            part.attributes["approach_place_config"] = approach_place_config
            part.attributes["place_config"] = place_config

            part.attributes["pick_trajectory"] = pick_trajectory
            part.attributes["place_trajectory"] = place_trajectory
            part.attributes["move_trajectory"] = move_trajectory

        except Exception:
            assembly.to_json("lecture_07/assembly_solved.json", pretty=True)

        # if i >= 50:
        #     print("Only testing, stop here")
        #     break

    assembly.to_json("lecture_07/assembly_solved.json", pretty=True)
