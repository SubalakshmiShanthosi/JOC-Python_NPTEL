# @Author: subalakshmi
# @Date:   2019-11-14T15:35:34+05:30
# @Last modified by:   subalakshmi
# @Last modified time: 2019-11-16T14:10:25+05:30

import networkx as nx
import random
import matplotlib.pyplot as plt
import operator
aGraph = nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(aGraph,with_labels=True)
plt.savefig('randomWalkGraph.png')
# Pick a random source node
x=random.choice([i for i in range(aGraph.number_of_nodes())])
# Counter stored in a dictionary - random walk Counter
dict_counter={}

# Initialise all nodes have walk length as zero
for i in range(aGraph.number_of_nodes()):
    dict_counter[i]=0

# 100 Random walks

for i in range(1000000):
    list_n=list(aGraph.neighbors(x))
    # If a node is sink pick some other node randomly from the given set of nodes in the graph
    if(len(list_n)==0):
        x=random.choice([i for i in range(aGraph.number_of_nodes())])
        dict_counter[x]=dict_counter[x]+1
    else:
        x=random.choice(list_n)
        dict_counter[x]=dict_counter[x]+1

pageRank=nx.pagerank(aGraph)
sorted_p=sorted(pageRank.items(),key=operator.itemgetter(1))
sorted_rand_walk=sorted(dict_counter.items(),key=operator.itemgetter(1))
print(sorted_p)
print('',end='\n')
print(sorted_rand_walk)
