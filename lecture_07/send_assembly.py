from compas.datastructures import Assembly
import compas_rrc as rrc
from compas_fab.robots import to_degrees
from helpers_2 import traverse


def send_trajectory(abb, speed, points, last_point_fine=True):
    for i in range(len(points)):
        c = points[i]
        joints = to_degrees(c.joint_values)
        if i < len(points) - 1:
            zone = rrc.Zone.Z10
        else:
            zone = rrc.Zone.FINE if last_point_fine else rrc.Zone.Z10

        abb.send(rrc.MoveToJoints(joints, ext_axes=[], speed=speed, zone=zone))

def get_assembly_sequence(assembly, top_course):
    sequence = []
    sequence_set = set(sequence)

    course_parts = list(
        assembly.graph.nodes_where_predicate(lambda key, attr: attr["part"].attributes["course"] == top_course)
    )

    for c in course_parts:
        parts = traverse(assembly, c)

        for part in reversed(parts):
            if part in sequence_set:
                continue
            sequence.append(part)
            sequence_set.add(part)
            part = assembly.find_by_key(part)

    return sequence

if __name__ == "__main__":
    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, "/rob1")
    print("Connected.")

    # Create Digital Inputs
    io_signal = "doUnitC141Out16"

    #set speed
    speed = 300

    assembly = Assembly.from_json("lecture_07/assembly_solved.json")
    print (len(list(assembly.parts())))

    for part in assembly.parts():
        
        top_course = assembly.attributes["courses"]
        sequence = get_assembly_sequence(assembly, top_course)
  
        if abb and abb.ros.is_connected:

            pick_trajectory = part.attributes["pick_trajectory"]
            if pick_trajectory == None:
                print(part.attributes["key"])
            move_trajectory = part.attributes["move_trajectory"]
            if move_trajectory == None:
                print(part.attributes["key"])
            place_trajectory = part.attributes["place_trajectory"]
            if place_trajectory == None:
                print(part.attributes["key"])
            total_points = len(pick_trajectory.points) * 2 + len(move_trajectory.points) * 2 + len(place_trajectory.points) * 2

            abb.send(rrc.PrintText("Sending {} PnP points. Press play to move".format(total_points)))
            # abb.send(rrc.Stop())

            speed = speed or 500
            send_trajectory(abb, speed, pick_trajectory.points)
            # abb.send(rrc.SetDigital(io_signal, 1))
            # abb.send(rrc.WaitTime(1))
            send_trajectory(abb, speed, list(reversed(pick_trajectory.points)), last_point_fine=False)
            send_trajectory(abb, speed, move_trajectory.points, last_point_fine=False)
            send_trajectory(abb, speed, place_trajectory.points)
            # abb.send(rrc.SetDigital(io_signal, 0))
            # abb.send(rrc.WaitTime(1))
            send_trajectory(abb, speed, list(reversed(place_trajectory.points)), last_point_fine=False)
            send_trajectory(abb, speed, list(reversed(move_trajectory.points)))

            print ("yeet")

    