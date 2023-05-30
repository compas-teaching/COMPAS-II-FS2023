from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import scale_vector, add_vectors, Point, Vector
from compas_slicer.geometry import Path
from random import randint
import math

def create_overhang_texture(slicer, overhang_distance):
    """Create a overhang texture
    """

    for i, layer in enumerate(slicer.layers):
        if i % 2 == 0 and i > 0:
            if i%4 == 0:
                tag = 0
                fac = i/5
            else:
                tag = 0
                fac = 1
            for j, path in enumerate(layer.paths):
                new_path1 = []
                for k, point1 in enumerate(path.points):
                    k = k-tag
                    if k % 2 == 0:
                        # get normal of point on polyline
                        normal = get_normal_of_path_on_xy_plane(k, point1, path, mesh=None)
                        normal_scaled = scale_vector(normal, -overhang_distance*fac)
                        new_pt1 = add_vectors(point1, normal_scaled)
                        # recreate point as compas point
                        point1 = Point(new_pt1[0], new_pt1[1], new_pt1[2])
                    # append point to new path
                    new_path1.append(point1)
                layer.paths[j] = Path(new_path1, is_closed=path.is_closed)