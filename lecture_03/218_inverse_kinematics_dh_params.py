from compas.geometry import Frame
from compas.robots import Joint
from compas.robots import RobotModel
from compas_fab.backends import AnalyticalInverseKinematics
from compas_fab.backends import OffsetWristKinematics
from compas_fab.backends.interfaces import ClientInterface
from compas_fab.robots import Robot

# create a custom robot model
model = RobotModel("custom-robot")
link1 = model.add_link("link1")
link2 = model.add_link("link2")
link3 = model.add_link("link3")
link4 = model.add_link("link4")
link5 = model.add_link("link5")
link6 = model.add_link("link6")
tool0 = model.add_link("tool0")

model.add_joint("shoulder_pan_joint", Joint.REVOLUTE, link1, link2, limit=(-6, 6))
model.add_joint("shoulder_lift_joint", Joint.REVOLUTE, link2, link3, limit=(-6, 6))
model.add_joint("elbow_joint", Joint.REVOLUTE, link3, link4, limit=(-6, 6))
model.add_joint("wrist_1_joint", Joint.REVOLUTE, link4, link5, limit=(-6, 6))
model.add_joint("wrist_2_joint", Joint.REVOLUTE, link5, link6, limit=(-6, 6))
model.add_joint("wrist_3_joint", Joint.REVOLUTE, link6, tool0, limit=(-6, 6))

client = ClientInterface()
client.inverse_kinematics = AnalyticalInverseKinematics()
client.inverse_kinematics.planner = OffsetWristKinematics(
    [
        0.1807,  # d1
        -0.6127,  # a2
        -0.57155,  # a3
        0.17415,  # d4
        0.11985,  # d5
        0.11655,  # d6
    ]
)

f = Frame((0.417, 0.191, -0.005), (-0.000, 1.000, 0.00), (1.000, 0.000, 0.000))

robot = Robot(model, client=client)
solutions = robot.iter_inverse_kinematics(f)

for jv in solutions:
    print(jv)
