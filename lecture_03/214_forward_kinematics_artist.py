from compas.artists import Artist
from compas.robots import RobotModel

model = RobotModel.ur5(load_geometry=True)

config = model.zero_configuration()
frame = model.forward_kinematics(config)

artist1 = Artist(frame)
artist2 = Artist(model)
artist2.update(config)

a = [artist1.draw()] + artist2.draw()
