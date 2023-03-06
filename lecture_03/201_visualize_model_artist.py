from compas.artists import Artist
from compas.robots import RobotModel

model = RobotModel.from_urdf_file("C:/Users/User/Documents/GitHub/COMPAS-II-FS2023/lecture_03/models/02_multipleshapes.urdf")

a = model
artist = Artist(model) #, layer="Robot"
#artist.clear_layer()
artist.draw_visual()
artist.redraw()
