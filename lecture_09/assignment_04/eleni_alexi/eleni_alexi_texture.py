import perlin
from compas_slicer.geometry import Path
from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import Point
from compas.geometry import scale_vector, add_vectors


def remap(value, low1, high1, low2, high2):
    return low2 + (value-low1)*(high2-low2)/(high1-low1)


def create_noise_texture(slicer, distance):
    """Creates a cool noise texture"""

    print("Creating a 3D noise texture")

    sn = perlin.SimplexNoise()

    for layer in slicer.layers:
        for j, path in enumerate(layer.paths):
            # create an empty layer in which we can store our modified points
            new_path = []
            for k, pt in enumerate(path.points):
                value = sn.noise3(pt[0]/100, pt[1]/100, pt[2]/100)
                # get the normal of the point in relation to the mesh
                normal = get_normal_of_path_on_xy_plane(k, pt, path, mesh=None)
                # scale the vector by a number to move the point
                normal_scaled = scale_vector(normal, value * distance)
                # create a new point by adding the point and the normal vector
                new_pt = add_vectors(pt, normal_scaled)
                # recreate the new_pt values as compas_points
                pt = Point(new_pt[0], new_pt[1], new_pt[2])

                # append the points to the new path
                new_path.append(pt)

            # replace the current path with the new path that we just created
            layer.paths[j] = Path(new_path, is_closed=path.is_closed)
