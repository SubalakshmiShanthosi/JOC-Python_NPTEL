# @Author: subalakshmi
# @Date:   2019-11-16T15:59:29+05:30
# @Last modified by:   subalakshmi
# @Last modified time: 2019-11-16T16:09:50+05:30
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


def assign_points(aGraph):
    nodes=list(aGraph.nodes())
    point=[]
    for each in nodes:
        point.append(100)
    return point


def distribute_points(aGraph,points):
    nodes=list(aGraph.nodes())
    new_points=[]
    # Getting part
    for i in range(len(nodes)):
        new_points.append(0)
    # Giving part
    for aNode in nodes:
        out=list(aGraph.out_edges(aNode))
        if(len(out)==0):
            new_points[aNode]=new_points[aNode]+points[aNode]
        else:
            share=points[aNode]/len(out)
            for (source,target) in out:
                new_points[target]=new_points[target]+share
    return new_points

def share_points(points,aGraph):
    nodes=list(aGraph.nodes())
    while(1):
        new_points=distribute_points(aGraph,points)
        print(new_points,end='\n')
        points=new_points
        stop=input("Press # to stop or any key to continue")
        if stop=='#':
            break
    return new_points


def rank_by_points(converged_points):
    aDict={}
    for i in range(len(converged_points)):
        aDict[i]=converged_points[i]
    #sortedDict=sorted(aDict.items(),key=operator.itemgetter(1))
    print(sorted(aDict.items(),key=lambda f:f[1]))


#Visualise aGraph
nx.draw(aGraph,with_labels=True)
plt.savefig('pointDisMetPageRank.png')

# Assign initial score for all points -- All nodes with 100 points each
points=assign_points(aGraph)

# Share points to neighbours equally
converged_points=share_points(points,aGraph)
print(converged_points)

# Rank by points
rank_by_points(converged_points)

# Default networkx pageRank

pageRankOutput=nx.pagerank(aGraph)
print(sorted(pageRankOutput.items(),key=lambda f:f[1]))
