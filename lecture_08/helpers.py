import math
from collections import deque


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


def generate_default_tolerances(joints):
    DEFAULT_TOLERANCE_METERS = 0.001
    DEFAULT_TOLERANCE_RADIANS = math.radians(1)

    return [DEFAULT_TOLERANCE_METERS if j.is_scalable() else DEFAULT_TOLERANCE_RADIANS for j in joints]
