import pandas as pd
import networkx as nx
from graph import *
import matplotlib.pyplot as plt

def import_graph1():
    header_list=["a","b","w"]
    E=pd.read_csv("Graph Data/bio-CE-CX.edges", sep=" ", header=None, names=header_list)
    G=nx.from_pandas_edgelist(E,"a","b",["w"])
    return G

def import_graph2():
    header_list=["a","b"]
    E=pd.read_csv("Graph Data/bio-dmela.mtx", sep=" ", header=None, names=header_list)
    G=nx.from_pandas_edgelist(E,"a","b")
    return G

def import_graph3():
    header_list=["a","b"]
    E=pd.read_csv("Graph Data/bio-grid-fruitfly.edges", sep=",", header=None, names=header_list)
    G=nx.from_pandas_edgelist(E,"a","b")
    return G

def import_graph4():
    header_list=["a","b"]
    E=pd.read_csv("Graph Data/bio-grid-human.edges", sep=",", header=None, names=header_list)
    G=nx.from_pandas_edgelist(E,"a","b")
    return G

def import_graph5():
    header_list=["a","b"]
    E=pd.read_csv("Graph Data/bio-grid-yeast.edges", sep=",", header=None, names=header_list)
    G=nx.from_pandas_edgelist(E,"a","b")
    return G

def graph_details(graph, graphName):
    print(f'--------------Details of {graphName}-------------')
    print("Number of Nodes",get_nodes(graph))
    print("Number of Edges",get_edges(graph))
    print("Graph Density",get_density(graph))
    # print("Graph Diameter",get_diameter(graph))
    print("Average Cluster Coefficient",avg_clustering_coeff(graph))

def plot_degree_distribution(graph):
    x,y=degree_of_distribution(graph)
    plt.plot(x,y)
    plt.xlabel("Degree")
    plt.ylabel("P(k)")
    plt.show()

if __name__=="__main__":
    graph1=import_graph1()
    graph2=import_graph2()
    graph3=import_graph3()
    graph4=import_graph4()
    graph5=import_graph5()
    # graph_details(graph1, "bio-CE-CX")
    # graph_details(graph2, "bio-dmela")
    # graph_details(graph3, "bio-grid-fruitfly")
    # graph_details(graph4, "bio-grid-human")
    graph_details(graph5, "bio-grid-yeast")
    # plot_degree_distribution(graph1)
    # plot_degree_distribution(graph2)
    # plot_degree_distribution(graph3)
    # plot_degree_distribution(graph4)
    # plot_degree_distribution(graph5)