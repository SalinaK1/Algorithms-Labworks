import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import math

def get_nodes(g): 
    return g.number_of_nodes()

def get_edges(g): 
    return g.number_of_edges()

def get_avg_degree(g):
    sum_of_degrees = 0
    for degree in g.degree():
        sum_of_degrees += degree[1]
    return (math.floor(sum_of_degrees/(get_nodes(g))))

def get_density(g):
    density = 0
    nodes = get_nodes(g)
    edges = get_edges(g)
    if nodes == 1:
        density = 0
    else:
        density = (2*edges)/(nodes*(nodes - 1))
    return density


def get_diameter(g):
    node_list = list(g.nodes)
    visited_nodes = []
    max_shortest_distance = 0
    try:
        for node1 in list(g.nodes):
            visited_nodes.append(node1)
            not_visited = list(set(node_list) - set(visited_nodes))
            for node2 in not_visited:
                shortest_distance = nx.shortest_path_length(g, node1, node2)
                if shortest_distance > max_shortest_distance:
                    max_shortest_distance = shortest_distance
        return max_shortest_distance
    except:
        return "Infinite path length because of disconnected graph"
    

def avg_clustering_coeff(g):
    if type(list(g.nodes.keys())[0]) == int:
        C = [0]*(max(g.nodes) +1)
    else:
        C = [0]*(len(g.nodes) +1)
    if (0 in g.nodes.keys()):
        first_index = 0
    else:
        first_index = 1
    for i in g.nodes:
        k = len(g.adj[i])
        if(k<2):
            if first_index: 
                C[int(i)-1] = 0
            else:
                C[int(i)] = 0
            continue

        e = 0
        
        for v in g.adj[i]:
            for u in g.adj[i]:
                if(v==u): continue

                if(g.has_edge(u,v)):
                    e+=1
        e = e/2
        clustering_coeff = (2*e)/(k*(k-1))
        if first_index: 
            C[int(i)-1] = clustering_coeff
        else:
            C[int(i)] = clustering_coeff
    avg_c_c = sum(C)/len(C)
    return avg_c_c


def degree_of_distribution(g):
    d=[]
    x=[]
    y=[]
    nodes=len(g.nodes())
    for i in g.nodes():
        degree=len(g.adj[i])
        d.append(degree)
    for i in range(0,max(d)+1):
        x.append(i)
        y.append((d.count(i)/nodes))
    return x,y


def plot_graph(g):
    edge_labels = dict([((n1, n2), d['weight'])
                        for n1, n2, d in g.edges(data=True)])

    pos = nx.spring_layout(g, k=0.3*1/np.sqrt(len(g.nodes())), iterations=900)  # Plot a less clustered graph
    plt.figure("Graph",figsize=(70, 57))                                        
    nx.draw(g, pos=pos, node_size=1000, 
            node_color='lightgreen', linewidths=0.25, font_size=19,               # Plotting the graph in spring layout
            font_weight='bold', with_labels=True)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels,               # Adding weighted edges
                                font_color='black', font_size=7, font_weight='bold')

    plt.show()


if __name__ == "__main__":
    G = nx.MultiGraph()                                                        

    with open("Graph Data/aves-sparrow-social.edges", "r") as f:                           # add nodes and edges in graph from input file
            lines = f.readlines()
            for line in lines:
                a, b, c = [c.strip() for c in line.split()][:3]
                G.add_edge(a, b, weight=float(c))
    
    print(f"No. of nodes in Graph: {get_nodes(G)}")
    print(f"No. of edges in Graph: {get_edges(G)}")
    print(f"Average degree of Graph: {get_avg_degree(G)}")
    print(f"Density of Graph: {get_density(G)}")
    print(f"Length of the shortest path between the most distanced nodes: {get_diameter(G)} edges")
    print(f"Average clusturing coefficient: {avg_clustering_coeff(G)}.")
    plot_graph(G)
