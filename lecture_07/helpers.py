import functools
from collections import deque

import compas_rhino
from compas.artists import Artist
from compas.utilities import color_to_colordict

colordict = functools.partial(color_to_colordict, colorformat="rgb", normalize=False)


def draw_directed_edges(artist, edges=None, color=None):
    node_xyz = artist.node_xyz
    edges = edges or list(artist.network.edges())
    edge_color = colordict(color, edges)
    lines = []
    for edge in edges:
        lines.append(
            {
                "start": node_xyz[edge[0]],
                "end": node_xyz[edge[1]],
                "color": edge_color[edge],
                "arrow": "end",
                "name": "{}.edge.{}-{}".format(artist.network.name, *edge),
            }
        )
    return compas_rhino.draw_lines(lines, layer=artist.layer, clear=False, redraw=False)


def traverse(assembly, k):
    tovisit = deque([k])
    visited = set([k])
    ordering = [k]
    while tovisit:
        node = tovisit.popleft()
        for nbr in assembly.graph.neighbors_in(node):
            if nbr not in visited:
                tovisit.append(nbr)
                visited.add(nbr)
                ordering.append(nbr)
    return ordering


def draw_parts(assembly):
    import compas_ghpython

    points = [{"pos": list(part.frame.point)} for part in assembly.parts()]
    return compas_ghpython.draw_points(points)


def draw_connections(assembly):
    import compas_ghpython

    lines = []

    for u, v in assembly.connections():
        u = assembly.find_by_key(u)
        v = assembly.find_by_key(v)
        lines.append(
            {
                "start": list(u.frame.point),
                "end": list(v.frame.point),
            }
        )
    return compas_ghpython.draw_lines(lines)


def draw_parts_attribute(assembly, attribute_name):
    return [Artist(p.attributes[attribute_name]).draw() for p in assembly.parts()]


def get_assembly_sequence(assembly, top_course):
    sequence = []
    sequence_set = set(sequence)

    course_parts = list(
        assembly.graph.nodes_where_predicate(lambda key, attr: attr["part"].attributes["course"] == top_course)
    )

    for c in course_parts:
        parts = traverse(assembly, c)

        for part in reversed(parts):
            if part in sequence_set:
                continue
            sequence.append(part)
            sequence_set.add(part)
            part = assembly.find_by_key(part)

    return sequence
