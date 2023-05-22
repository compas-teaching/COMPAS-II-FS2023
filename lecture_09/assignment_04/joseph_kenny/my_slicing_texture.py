from compas_slicer.geometry import Path
from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import Point
from compas.geometry import scale_vector, add_vectors

def create_overhang_texture(slicer, overhang_distance):
    """Creates a cool overhang texture"""

    for i, layer in enumerate(slicer.layers):

        for j, path in enumerate(layer.paths):
            
            # create an empty layer in which we can store our modified points
            new_path = []

            for k, pt in enumerate(path.points):
                # get the normal of the point in relation to the mesh
                normal = get_normal_of_path_on_xy_plane(k, pt, path, mesh=None)

                # If the point is in the middle third of the list move
                if k >= (len(path.points)/3) and k <= ((len(path.points)/3)*2):
                    # scale the vector by a number to move the point
                    normal_scaled = scale_vector(normal, -overhang_distance)
                    # create a new point by adding the point and the normal vector
                    new_pt = add_vectors(pt, normal_scaled)
                    # recreate the new_pt values as compas_points
                    pt = Point(new_pt[0], new_pt[1], new_pt[2])

                # If the point is in the 5th layer and second point move
                elif i % 5 == 0 and i > 0 and k % 2 == 0:
                        # scale the vector by a number to move the point
                        normal_scaled = scale_vector(normal, -overhang_distance)
                        # create a new point by adding the point and the normal vector
                        new_pt = add_vectors(pt, normal_scaled)
                        # recreate the new_pt values as compas_points
                        pt = Point(new_pt[0], new_pt[1], new_pt[2])

                # append the points to the new path
                new_path.append(pt)

            # replace the current path with the new path that we just created
            layer.paths[j] = Path(new_path, is_closed=path.is_closed)


