
from compas_occ.geometry import OCCNurbsCurve

def path_smooth(slicer, smooth_distance):

    print("Creating path smooth ...")
    for i, layer in enumerate(slicer.layers):
        for j, path in enumerate(layer.paths):
            curve = OCCNurbsCurve.from_points(path.points, 3)
            ts = curve.divide_by_length(smooth_distance)
            path.points = [curve.point_at(t) for t in ts]

