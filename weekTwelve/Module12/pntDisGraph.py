# @Author: subalakshmi
# @Date:   2019-11-16T15:18:31+05:30
# @Last modified by:   subalakshmi
# @Last modified time: 2019-11-16T15:30:30+05:30

import networkx as nx
import random
import matplotlib.pyplot as plt

def add_edges(aGraph):
    nodes=list(aGraph.nodes())
    for source in nodes:
        for target in nodes:
            if source != target:
                randProb=random.random()
                if randProb<=0.5:
                    aGraph.add_edge(source,target)
    return aGraph

aGraph=nx.DiGraph()
aGraph.add_nodes_from([i for i in range(10)])
aGraph=add_edges(aGraph)

#Visualise aGraph
nx.draw(aGraph,with_labels=True)
plt.savefig('pointDisGraph.png')
