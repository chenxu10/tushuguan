# --------------------------------------------------------------------
# This script draws a network of ShiYou you learn from,
# you play with, you compete with and you teach
# 
#
# --------------------------------------------------------------------

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

edges = [("Me","Chenzhong Hua"),
         ("Me","Nassim Nicholas Taleb"),
         ("Chenzhong Hua","Junsheng Hong"),
         ("Me","Hejing Han"),
         ("Me","Xiangming Yuan"),
         ("Me","Dmitri Kudryashov"),
         ("Me","Charlie L"),
         ("Charlie L","ShengShyan Huang"),
         ("Dmitri Kudryashov","Adam Mizner"),
         ("Adam Mizner","ShengShyan Huang"),
         ("ShengShyan Huang","Man-ching Cheng"),
         ("Xiangming Yuan","Jiajun Jiang"),
         ("Jiajun Jiang","Junsheng Hong"),
         ("Zhiping Yang","Yangming Wang"),
         ("Me","Zhiping Yang"),
         ("Me","Charlie Munger"),
         ("Me","Josh Hug"),
         ("Me","John DeNero")]
G.add_edges_from(edges)
nx.draw(
    G,
    with_labels=True
)
plt.show()