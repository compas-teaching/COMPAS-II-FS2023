from compas_slicer.geometry import Path
from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import Point
from compas.geometry import scale_vector, add_vectors

def create_overhang_texture(slicer, overhang_distance):
    print("Creating overhang texture...")

    for i, layer in enumerate(slicer.layers):
        if i%7 == 0 and i > 0:
            # only take every 7th layer and ignore the first one
            for j, path in enumerate(layer.paths):

                new_path = []
                for k, pt in enumerate(path.points):
                    if k%2 == 0:
                        normal = get_normal_of_path_on_xy_plane(k, pt, path, mesh=None)
                        normal_scaled = scale_vector(normal, -overhang_distance)
                        new_pt = add_vectors(pt, normal_scaled)
                        new_compas_pt = Point(*new_pt)
                        new_path.append(new_compas_pt)
                    else:
                        new_path.append(pt)

                layer.paths[j] = Path(new_path, is_closed=path.is_closed)
