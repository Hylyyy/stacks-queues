import networkx as nx
print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")


graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["london"])
