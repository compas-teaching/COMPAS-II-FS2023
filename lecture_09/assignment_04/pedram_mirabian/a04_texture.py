from compas_slicer.geometry import Path
from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import Point
from compas.geometry import scale_vector, add_vectors
from compas.geometry import Vector

def distort(slicer, shift):
    for layer_index, layer in enumerate(slicer.layers):

        for path_index, path in enumerate(layer.paths):
            
            mod_path = []
            pt_count = len(path.points)
            for point_index, point in enumerate(path.points):
                
                base = Point(0,0,0)
                radius_vec = Vector.from_start_end(base, point)
                radius_vec = Vector(radius_vec[0], radius_vec[1], 0)
                radius_vec.unitize()
                
                vector = scale_vector(radius_vec, (point_index%(pt_count/4))*shift)
                mod_point = add_vectors(point, vector)
                point = Point(mod_point[0], mod_point[1], mod_point[2])
                mod_path.append(point)

        layer.paths[path_index] = Path(mod_path, is_closed=path.is_closed)
