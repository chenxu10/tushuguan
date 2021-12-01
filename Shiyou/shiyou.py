# --------------------------------------------------------------------
# This script draws a network of ShiYou you learn from,
# you play with, you compete with and you teach
# 
# Author: Xu Shen(xs286@cornell.edu)
# 
# --------------------------------------------------------------------

from networkx.algorithms import community

import matplotlib.pyplot as plt
import networkx as nx

# G = nx.Graph()
edges = [("Me","Chenzhong Hua"),
         ("Me","Nassim Nicholas Taleb"),
         ("Nassim Nicholas Taleb", "Edward O.Thorp"),
         ("Chenzhong Hua","Junsheng Hong"),
         ("Me","Jinghan He"),
         ("Me","Xiangming Yuan"),
         ("Me","Dmitri Kudryashov"),
         ("Me","Charlie L"),
         ("Charlie L","ShengShyan Huang"),
         ("Dmitri Kudryashov","Adam Mizner"),
         ("Adam Mizner","ShengShyan Huang"),
         ("ShengShyan Huang","Man-ching Cheng"),
         ("Xiangming Yuan","Junsheng Hong"),
         ("Zhiping Yang","Yangming Wang"),
         ("Me","Zhiping Yang"),
         ("Zhiping Yang","Robert A. Bjork"),
         ("Me","Charlie Munger"),
         ("Me","Josh Hug"),
         ("Me","John DeNero"),
         ("Me","George Polya"),
         ("Me","Herbert Simon"),
         ("Me","Robert A. Bjork"),
         ("Jinghan He","Man-ching Cheng")]
    
# G.add_edges_from(edges)
#edges = [['A', 'B'], ['B', 'C'], ['B', 'D']]
G = nx.Graph()
G.add_edges_from(edges)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(
    G, pos, edge_color='black', width=1, linewidths=1,
    node_size=500, node_color='pink', alpha=0.9,
    labels={node: node for node in G.nodes()}
)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={
        ('Jinghan He', 'Me'): 'Sacrum-Dang-Stretch Jing-Pelvis',
        ('Josh Hug','Me'):'Patterns Abstraction',
    },
    font_color='red'
)
plt.show()
