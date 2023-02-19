import random

import compas
from compas.artists import Artist
from compas.datastructures import Network

network = Network.from_obj(compas.get("grid_irregular.obj"))

# Select random node + neighbors
node = random.choice(list(network.nodes()))
nbrs = network.neighbors(node)

facecolor = {node: (1.0, 0.0, 0.0)}
for nbr in nbrs:
    facecolor[nbr] = (0.0, 0.0, 1.0)

edgecolor = {}
for nbr in nbrs:
    edgecolor[node, nbr] = (1.0, 0.0, 0.0)
    edgecolor[nbr, node] = (1.0, 0.0, 0.0)

print(network.summary())

text = {node: network.node_attribute(node, "weight") for node in network.nodes()}

artist = Artist(network, layer="network")
artist.clear_layer()
artist.draw_nodes(color=facecolor)
artist.draw_nodelabels()
artist.draw_edges(color=edgecolor)
