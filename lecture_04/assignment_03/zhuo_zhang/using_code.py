from compas.artists import Artist
from compas.geometry import Frame
from compas_fab.backends import RosClient
from compas_rhino.conversions import plane_to_compas_frame, RhinoMesh
from compas_fab.robots import Tool

with RosClient("localhost") as client:
    robot = client.load_robot(load_geometry=True)
    group = robot.main_group_name

    # Attach tool
    mesh = RhinoMesh.from_geometry(mesh).to_compas()
    tool = Tool(mesh, plane_to_compas_frame(tcf_plane), mesh)
    robot.attach_tool(tool)

    # Start configuration
    start_configuration = robot.inverse_kinematics(plane_to_compas_frame(pick_up_plane))

    # Target planes
    frames = []
    for f in target_planes:
        frames.append(plane_to_compas_frame(f))

    # Cartesian motion
    trajectory = robot.plan_cartesian_motion(
        frames,
        start_configuration
    )

    print("Fraction = " + str(trajectory.fraction))
