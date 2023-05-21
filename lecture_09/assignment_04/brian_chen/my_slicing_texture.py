from compas_slicer.geometry import Path
from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import Point
from compas.geometry import scale_vector, add_vectors

def create_overhang_texture(slicer, overhang_distance):
    print("create_overhang_texture")



    for i,layer in enumerate(slicer.layers):
        if i%3 == 0 and i>0:
            for j,path in enumerate(layer.paths):

                new_path_f = []
                for k , pt in enumerate(path.points):

                    if k %4 ==0:
                        normal = get_normal_of_path_on_xy_plane(k,pt,path, mesh=None)
                        normal_scaled = scale_vector(normal, -overhang_distance)
                        new_pt = add_vectors(pt,normal_scaled)

                        new_compas_pt = Point(new_pt[0], new_pt[1], new_pt[2])
                        new_path_f.append(new_compas_pt)
                    else:
                        new_path_f.append(pt)

                layer.paths[j] = Path(new_path_f, is_closed=path.is_closed)

        else:
            i%3 != 0 and i>0
            for j,path in enumerate(layer.paths):

                new_path_s = []
                for k , pt in enumerate(path.points):
                    if k %2 ==0:
                        normal = get_normal_of_path_on_xy_plane(k,pt,path, mesh=None)
                        normal_scaled = scale_vector(normal, -15)
                        new_pt = add_vectors(pt,normal_scaled)

                        new_compas_pt = Point(new_pt[0], new_pt[1], new_pt[2])
                        new_path_s.append(new_compas_pt)
                    else:
                        new_path_s.append(pt)

                layer.paths[j] = Path(new_path_s, is_closed=path.is_closed)
                
