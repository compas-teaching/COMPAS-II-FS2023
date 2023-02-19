from compas.utilities import pairwise
import random

import compas
from compas.artists import Artist
from compas.datastructures import Network

network = Network.from_obj(compas.get("grid_irregular.obj"))

# Select random nodes + shortest path
start = random.choice(list(network.leaves()))
goal = random.choice(list(set(network.leaves()) - set([start])))
nodes = network.shortest_path(start, goal)

nodecolor = {}
edgecolor = {}

for u, v in pairwise(nodes):
    nodecolor[v] = (0.0, 1.0, 0.0)
    edgecolor[u, v] = edgecolor[v, u] = (0.0, 1.0, 0.0)

nodecolor[start] = (1.0, 0.0, 0.0)
nodecolor[goal] = (0.0, 0.0, 1.0)

print(network.summary())

artist = Artist(network, layer="network")
artist.clear_layer()
artist.draw_nodes(color=nodecolor)
artist.draw_nodelabels()
artist.draw_edges(color=edgecolor)
