import networkx as nx
import time
from concurrent.futures import ThreadPoolExecutor

def parallel_scc(graph):
    """
    Simulated parallel SCC detection using forward-backward reachability.
    This is not truly parallel due to Python's GIL, but structured as such.
    """
    def trim_graph(G):
        # Remove nodes with no in-edges or out-edges
        changed = True
        while changed:
            changed = False
            to_remove = [node for node in G.nodes if G.in_degree(node) == 0 or G.out_degree(node) == 0]
            if to_remove:
                G.remove_nodes_from(to_remove)
                changed = True
        return G

    def get_fw_bw_scc(G, pivot):
        # Forward and backward reachable sets
        fw = set(nx.descendants(G, pivot))
        bw = set(nx.ancestors(G, pivot))
        fw.add(pivot)
        bw.add(pivot)
        return fw & bw  # SCC is intersection

    def recursive_scc(G):
        if G.number_of_nodes() == 0:
            return []

        G = trim_graph(G.copy())

        if G.number_of_nodes() == 0:
            return []

        pivot = next(iter(G.nodes))
        scc = get_fw_bw_scc(G, pivot)

        # Remove the found SCC and split the graph
        G.remove_nodes_from(scc)
        rest = list(nx.weakly_connected_components(G))

        sccs = [list(scc)]

        # Recurse on disconnected components in parallel
        subgraphs = [G.subgraph(c).copy() for c in rest]

        with ThreadPoolExecutor() as executor:
            results = executor.map(recursive_scc, subgraphs)
            for result in results:
                sccs.extend(result)

        return sccs

    return recursive_scc(graph)

# Example usage
if __name__ == "__main__":
    num_nodes = 25000
    edge_prob = 0.03

    G = nx.gnp_random_graph(num_nodes, edge_prob, directed=True)
    print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    start = time.time()
    sccs = parallel_scc(G)
    end = time.time()

    print(f"\nParallel SCC Simulation:")
    print(f"Total SCCs found: {len(sccs)}")
    print(f"Execution time: {end - start:.4f} seconds")
