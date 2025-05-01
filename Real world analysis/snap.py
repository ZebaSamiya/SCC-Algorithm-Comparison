import networkx as nx

def load_directed_graph(filename):
    G = nx.DiGraph()
    
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("#") or line.strip() == "":
                continue  # skip comments and empty lines
            from_node, to_node = map(int, line.strip().split())
            G.add_edge(from_node, to_node)
    
    return G

# Usage
graph = load_directed_graph('snap.txt')

# Optional: Print basic info
print("Number of nodes:", graph.number_of_nodes())
print("Number of edges:", graph.number_of_edges())