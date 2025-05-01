import sys
sys.setrecursionlimit(1000000)

import networkx as nx
import time
import statistics

def generate_directed_erdos_renyi_graph(n, p, seed=None):
    """
    Generate a directed Erdős–Rényi random graph with n nodes and edge probability p.
    """
    return nx.gnp_random_graph(n=n, p=p, seed=seed, directed=True)

def tarjans_scc(graph):
    index = 0
    index_map = {}
    lowlink_map = {}
    stack = []
    on_stack = set()
    sccs = []

    def strongconnect(node):
        nonlocal index
        index_map[node] = index
        lowlink_map[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)

        for neighbor in graph.successors(node):
            if neighbor not in index_map:
                strongconnect(neighbor)
                lowlink_map[node] = min(lowlink_map[node], lowlink_map[neighbor])
            elif neighbor in on_stack:
                lowlink_map[node] = min(lowlink_map[node], index_map[neighbor])

        if lowlink_map[node] == index_map[node]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == node:
                    break
            sccs.append(scc)

    for node in graph.nodes:
        if node not in index_map:
            strongconnect(node)

    return sccs

def kosaraju_scc(graph):
    visited = set()
    finish_stack = []

    def dfs_first(node):
        visited.add(node)
        for neighbor in graph.successors(node):
            if neighbor not in visited:
                dfs_first(neighbor)
        finish_stack.append(node)

    for node in graph.nodes:
        if node not in visited:
            dfs_first(node)

    reversed_graph = graph.reverse(copy=True)
    visited.clear()
    sccs = []

    def dfs_second(node, scc):
        visited.add(node)
        scc.append(node)
        for neighbor in reversed_graph.successors(node):
            if neighbor not in visited:
                dfs_second(neighbor, scc)

    while finish_stack:
        node = finish_stack.pop()
        if node not in visited:
            scc = []
            dfs_second(node, scc)
            sccs.append(scc)

    return sccs

if __name__ == "__main__":
    num_nodes = 25000
    edge_prob = 0.03
    trials = 10

    tarjan_times = []
    kosaraju_times = []

    for i in range(trials):
        print(f"\n🔁 Trial {i+1}/{trials}")
        G = generate_directed_erdos_renyi_graph(num_nodes, edge_prob, seed=i)
        print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

        # Tarjan's
        start = time.time()
        tarjans_result = tarjans_scc(G)
        end = time.time()
        t_time = end - start
        tarjan_times.append(t_time)
        print(f"Tarjan's time: {t_time:.4f}s | SCCs: {len(tarjans_result)}")

        # Kosaraju's
        start = time.time()
        kosaraju_result = kosaraju_scc(G)
        end = time.time()
        k_time = end - start
        kosaraju_times.append(k_time)
        print(f"Kosaraju's time: {k_time:.4f}s | SCCs: {len(kosaraju_result)}")

    print("\n✅ AVERAGE OVER 10 TRIALS:")
    print(f"Tarjan's Avg Time: {statistics.mean(tarjan_times):.4f} seconds")
    print(f"Kosaraju's Avg Time: {statistics.mean(kosaraju_times):.4f} seconds")
