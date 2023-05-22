from compas_slicer.geometry import Path
from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import Point
from compas.geometry import scale_vector, add_vectors

def create_cool_texture(slicer, overhang_percentage):
    """Creates a cool texture"""

    print("*****Texturisation is happening in a cool way...*****")

    for i, layer in enumerate(slicer.layers):
        if i % 3 == 0 and i > 0:
            for j, path in enumerate(layer.paths):
                new_path = []
                for k, pt in enumerate(path.points):
                    if k % 6 in range(3, 7):
                        normal = get_normal_of_path_on_xy_plane(k, pt, path, mesh=None)
                        # Create gap in wall surface by drawing points backwards
                        #   and add rigidity to the print by creating corrugations
                        # Could look really cool with some light inside
                        normal_scaled = scale_vector(normal, overhang_percentage)
                        new_pt = add_vectors(pt, normal_scaled)
                        new_compas_pt = Point(*new_pt)
                        new_path.append(new_compas_pt)
                    else:
                        new_path.append(pt)
                    layer.paths[j] = Path(new_path, is_closed=path.is_closed)


def create_cool_texture_example(slicer, overhang_distance):
    """Creates a cool texture"""

    print("Creating cool texture")

    for i, layer in enumerate(slicer.layers):
        if i % 5 == 0 and i > 0:
            # for every 5th layer, except for the first layer
            # print(layer)
            for j, path in enumerate(layer.paths):
                # print(path)
                # create an empty layer in which we can store our modified points
                new_path = []
                for k, pt in enumerate(path.points):
                    # for every second point (only even points)
                    if k % 2 == 0:
                        # get the normal of the point in relation to the mesh
                        normal = get_normal_of_path_on_xy_plane(k, pt, path, mesh=None)
                        # scale the vector by a number to move the point
                        normal_scaled = scale_vector(normal, -overhang_distance)
                        # create a new point by adding the point and the normal vector
                        new_pt = add_vectors(pt, normal_scaled)
                        # recreate the new_pt values as compas_points
                        # new_compas_pt = Point(new_pt[0], new_pt[1], new_pt[2])
                        new_compas_pt = Point(*new_pt)  # Fancy version, taking the direct reference
                        # append the points to the new path
                        new_path.append(new_compas_pt)
                    else:
                        new_path.append(pt)

                # replace the current path with the new path that we just created
                layer.paths[j] = Path(new_path, is_closed=path.is_closed)
