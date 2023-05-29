"""
Calculate pickup of a part.
"""

from compas.geometry import Frame
from compas_fab.robots import PlanningScene
from compas.robots import Configuration
import math
import os
from copy import deepcopy
from compas import json_dump,json_load
from compas_fab.backends import RosClient
from compas_fab.robots import Tool

def reverse_trajectory(trajectory):
    out_trajectory = deepcopy(trajectory)
    out_trajectory.points = list(reversed(trajectory.points))
    return out_trajectory



with RosClient("localhost") as client:
    robot = client.load_robot()
    scene = PlanningScene(robot)
    tolerance_above = 0.001
    tolerance_below = 0.001
    all_trajectories = []
    

    data = json_load(r'\Users\josep\OneDrive\Desktop\mas_dfab_22_23\compas_ii_intro_course\COMPAS-II-FS2023\lecture_07\trial_testing\data_elv.json')
    group, c_visual_mesh, tcf_frame, assembly, pick_frame, approach_distance, planner_id = data['group'], data['c_visual_mesh'], data['tcf_frame'], data['assembly'], data['pick_frame'], data['approach_distance'], data['planner_id']
    tool = Tool(c_visual_mesh, tcf_frame, c_visual_mesh)
    robot.attach_tool(tool, group)
    """
    Pick trajectory
    """
    approach_pick_frame = Frame(pick_frame.point +(pick_frame.normal*approach_distance), pick_frame.xaxis, pick_frame.yaxis)

    start_configuration = Configuration.from_revolute_values([0,0,0,0,math.pi/2,0])
    approach_pick_config = robot.inverse_kinematics(approach_pick_frame, start_configuration, group)
    pick_config = robot.inverse_kinematics(pick_frame, approach_pick_config, group)

    
    goal_constraints = robot.constraints_from_configuration(configuration=pick_config, tolerances_above=[tolerance_above], tolerances_below=[tolerance_below], group=group)
    pick_trajectory = robot.plan_motion(
        goal_constraints,
        start_configuration=approach_pick_config,
        group=group,
        options=dict(
            planner_id=planner_id,
        ),
    )

    print ('start planning with ' + planner_id+'...')
    for i in range(assembly.attributes['count']):
    # for i in range(0,18):
        print ('Planning part %d successfully' % i)

        """
        Place
        """
        part = assembly.find_by_key(i)
        place_frame = part.attributes['place_frame']
        approach_place_frame = Frame(place_frame.point + [0, 0, approach_distance], place_frame.xaxis, place_frame.yaxis)

        approach_place_config = robot.inverse_kinematics(approach_place_frame, start_configuration, group)
        place_config = robot.inverse_kinematics(place_frame, approach_place_config, group)

        
        goal_constraints = robot.constraints_from_configuration(configuration=place_config, tolerances_above=[tolerance_above], tolerances_below=[tolerance_below], group=group)
        place_trajectory = robot.plan_motion(
            goal_constraints,
            start_configuration=approach_place_config,
            group=group,
            options=dict(
                planner_id=planner_id,
            ),
        )

        ''' 
        Pick to place
        '''
        goal_constraints = robot.constraints_from_configuration(configuration=approach_place_config, tolerances_above=[tolerance_above], tolerances_below=[tolerance_below], group=group)
        pick_to_place_trajectory = robot.plan_motion(
            goal_constraints,
            start_configuration=approach_pick_config,
            group=group,
            options=dict(
                planner_id=planner_id,
            ),
        )

        all_trajectories.extend( [pick_trajectory, reverse_trajectory(pick_trajectory), pick_to_place_trajectory, place_trajectory, reverse_trajectory(place_trajectory),reverse_trajectory(pick_to_place_trajectory)])
        # all_trajectories.extend( [ place_config])


json_dump(all_trajectories, 'trajectories.json', True)
print ('Trajectories saved successfully in trajectories.json')
