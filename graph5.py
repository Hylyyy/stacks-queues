print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

print(nodes["london"])








print(graph)
