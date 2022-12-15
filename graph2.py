print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

import networkx as nx
graph = nx.nx_agraph.read_dot("roadmap.dot")
graph.nodes["london"]
