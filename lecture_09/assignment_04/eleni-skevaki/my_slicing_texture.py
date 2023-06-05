from compas_slicer.geometry import Path
from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import Point
from compas.geometry import scale_vector, add_vectors
import math


class SinusFunction:
    def __init__(self, frequency, amplitude=1, phase=0, offset=0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase
        self.offset = offset

    def getValue(self, value):
        return math.sin(self.frequency * value + self.phase) * self.amplitude + self.offset


def create_overhang_texture(slicer, overhang_distance):
    """Creates a zigzig texture"""

    print("Creating cool texture")

    for i, layer in enumerate(slicer.layers):
        for j, path in enumerate(layer.paths):
            new_path = []
            for k, pt in enumerate(path.points):
                pFreq = 10
                pAmp = 5 * (1 + 0.05* i)
                pPhase = 0.0
                pOffset = 0.0

                pFunction = SinusFunction(pFreq, pAmp, pPhase, pOffset)
                pos_p = (1.0 * k / len(path.points)) * 2.0 * math.pi
                mag_p = pFunction.getValue(pos_p)

                if i % 2 == 0:
                    magnitude = mag_p
                else:
                    magnitude = -mag_p

                # get the normal of the point in relation to the mesh
                normal = get_normal_of_path_on_xy_plane(k, pt, path, mesh=None)
                # scale the vector by a number to move the point
                normal_scaled = scale_vector(normal, -magnitude)
                # create a new point by adding the point and the normal vector
                new_pt = add_vectors(pt, normal_scaled)
                # recreate the new_pt values as compas_points
                pt = Point(*new_pt)

                # append the points to the new path
                new_path.append(pt)

            # replace the current path with the new path that we just created
            layer.paths[j] = Path(new_path, is_closed=path.is_closed)
