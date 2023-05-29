import compas_rrc as rrc
from compas_fab.robots import to_degrees
from compas import json_load
from compas_fab.backends import RosClient
from compas_fab.robots import PlanningScene
from compas_fab.robots import Tool


io_signal = 'doUnitC141Out16'
speed = 200


def send_trajectory(abb, robot, speed, points, last_point_fine=True):
    for i in range(len(points)):
        c = points[i]
        joints = to_degrees(c.joint_values)
        if i < len(points) - 1:
            zone = rrc.Zone.Z10
        else:
            zone = rrc.Zone.FINE if last_point_fine else rrc.Zone.Z10

        abb.send(rrc.MoveToJoints(joints, ext_axes=[], speed=speed, zone=zone))


with RosClient("localhost") as client:
    robot = client.load_robot()
    scene = PlanningScene(robot)

    data = json_load(r'C:\Users\josep\OneDrive\Desktop\mas_dfab_22_23\compas_ii_intro_course\COMPAS-II-FS2023\lecture_07\trial_testing\data_elv.json')
    group, c_visual_mesh, tcf_frame, assembly, pick_frame, approach_distance, planner_id = data['group'], data['c_visual_mesh'], data['tcf_frame'], data['assembly'], data['pick_frame'], data['approach_distance'], data['planner_id']
    tool = Tool(c_visual_mesh, tcf_frame, c_visual_mesh)
    robot.attach_tool(tool, group)

    abb = rrc.AbbClient(client)
    trajectories = json_load(r'C:\Users\josep\OneDrive\Desktop\mas_dfab_22_23\compas_ii_intro_course\COMPAS-II-FS2023\lecture_07\trial_testing\trajectories.json')

    abb.send(rrc.PrintText("Sending {} PnP points. Press play to move".format(len(trajectories))))
    abb.send(rrc.Stop())

    for i in range(int(len(trajectories)/6)):
        send_trajectory(abb, robot, speed, trajectories[6*i].points)
        abb.send(rrc.SetDigital(io_signal, 1))
        abb.send(rrc.WaitTime(1))
        send_trajectory(abb, robot, speed, trajectories[6*i+1].points, last_point_fine=False)
        send_trajectory(abb, robot, speed, trajectories[6*i+2].points, last_point_fine=False)
        send_trajectory(abb, robot, speed,trajectories[6*i+3].points)
        abb.send(rrc.SetDigital(io_signal, 0))
        abb.send(rrc.WaitTime(1))
        send_trajectory(abb, robot, speed, trajectories[6*i+4].points, last_point_fine=False)
        send_trajectory(abb, robot, speed, trajectories[6*i+5].points)
