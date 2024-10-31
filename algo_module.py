import pandas as pd
from graph import Graph


HEAD_OF_QUEUE = 0


def bfs(g: Graph, s: int) -> tuple[dict, dict]:
    """
    BFS algorithm.
    Args:
        g (Graph): a Graph object.
        s (int): name of source vertex.
    """
    # set initial values
    visited = []
    dist = {}
    bfs_tree = {}
    visited.append(s)
    dist[s] = 0
    bfs_tree[s] = None
    Q = [s]  # queue of vertices to scan.
    # traverse graph
    while Q:  # while Q is not empty.
        u = Q[HEAD_OF_QUEUE]
        v = g.get_adj_list_by_name(u)  # head of neighbors list of u.
        for i in range(g.out_deg(u)):
            if v.get_data() not in visited:
                visited.append(v.get_data())
                dist[v.get_data()] = dist[u] + 1
                bfs_tree[v.get_data()] = u
                Q.append(v.get_data())
            v = v.get_next()
        Q.remove(u)
        visited.append(u)
    return dist, bfs_tree


def dfs(g: Graph) -> tuple[dict, dict, dict]:
    """
    DFS algorithm.
    Args:
        g (Graph): a graph.
    """
    # set initial values
    time = 0
    visited = []
    discovery_times = {}
    finish_times = {}
    dfs_forest = {}
    # traverse graph
    for i in range(g.get_size()):
        if g.get_node(i) not in visited:
            dfs_forest[g.get_node(i)] = None
            time = __dfs_visit(g, g.get_node(i), time, visited, discovery_times, finish_times, dfs_forest)
    return discovery_times, finish_times, dfs_forest


def __dfs_visit(g: Graph, u: int, time: int, visited: list, discovery_times: dict, finish_times: dict, dfs_forest: dict):
    """
    Args:
        g (Graph): a Graph object.
        u (int): name of source vertex.
        time (int): current global time.
        visited (list): list of names of visited nodes.
        discovery_times (dict): dictionary of node : time pairs
        finish_times (dict): dictionary of node : time pairs.
        dfs_forest (dict): dictionary of node : parent pairs.

    Returns:
        int: current global time.
    """
    time += 1
    discovery_times[u] = time
    visited.append(u)
    v = g.get_adj_list_by_name(u)  # head of neighbors list of u.
    for i in range(g.out_deg(u)):
        if v.get_data() not in visited:
            dfs_forest[v.get_data()] = u
            time = __dfs_visit(g, v.get_data(), time, visited, discovery_times, finish_times, dfs_forest)
        v = v.get_next()
    time += 1
    finish_times[u] = time
    return time


def __transpose_edges(g: Graph):
    """
    creates a list of transposed edges.
    Args:
        g (Graph): a Graph object.

    Returns:
        list of tuples (n, m, w), where there's an edge from n to m with weight w.
    """
    edges = []
    for i in range(g.get_size()):
        n = g.get_node(i)
        m = g.get_adj_list_by_name(n)  # head of neighbors list.
        for j in range(g.out_deg(n)):
            edges.append((m.get_data(), n, m.get_weight()))
            m = m.get_next()
    return edges


def __get_trees_list(dfs_forest: dict) -> list[list]:
    """
    Args:
        dfs_forest (dict): dictionary of node : parent pairs in a dfs forest.

    Returns:
        list[list]: list of lists, each contains nodes in a unique tree.
    """
    trees = [[key] for key in dfs_forest if dfs_forest[key] == None]
    for i in range(len(trees)):
        __helper(dfs_forest, trees, *trees[i], i)
    return trees


def __helper(dfs_forest, trees, n, idx):
    for key in dfs_forest:
        if dfs_forest[key] == n:
            trees[idx].append(key)
            __helper(dfs_forest, trees, key, idx)


def strongly_connected_components(g: Graph) -> list[list]:
    """
    Use Kosaraju-Sharir algorithm to get strongly connected components of graph.

    Args:
        g (Graph): a Graph object.

    Returns:
        list[list]: list of strongly connected components.
    """
    discovery_times, finish_times, dfs_forest = dfs(g)
    # sort nodes by decreasing finish times
    nodes = list(dict(sorted(finish_times.items(), key=lambda item: item[1], reverse=True)).keys())
    # compute transpose of graph
    edges = __transpose_edges(g)
    g_transpose = Graph(nodes, edges)
    # run dfs on transpose of graph using sorted order in main loop
    discovery_times, finish_times, dfs_forest = dfs(g_transpose)
    # report each dfs tree as a strongly connected component
    return __get_trees_list(dfs_forest)
    
    
def transpose_graph(g: Graph) -> Graph:
    """
    Args:
        g (Graph): a Graph object.

    Returns:
        Graph: transpose of g.
    """
    edges = __transpose_edges(g)
    nodes = g.get_nodes()
    return Graph(nodes, edges)


def strongly_connected_graph(g: Graph) -> Graph:
    """
    strongly connected graph G_SCC of a directed graph G is a graph where:
    (1) each strongly connected component of G has one node in G_SCC.
    (2) each edge (u, v) in G, such that u and v are in different strongly connected components,
    has an edge between the appropriate nodes in G_SCC.

    Args:
        g (Graph): a Graph object.

    Returns:
        Graph: strongly connected graph of g.
    """
    scc = strongly_connected_components(g)
    nodes = [i for i in range(len(scc))]
    
    edges = []
    for i in range(g.get_size()):
        u = g.get_node(i)
        v = g.get_adj_list_by_name(u)  # head of neighbors list.
        for i in range(g.out_deg(u)):
            # find scc of u and v
            u_scc = 0
            v_scc = 0
            for j in range(len(scc)):
                if u in scc[j]:
                    u_scc = j
                if v.get_data() in scc[j]:
                    v_scc = j
            # if u and v are in different strongly connected components, add edge to edges list
            if u_scc != v_scc:
                edges.append((u_scc, v_scc, v.get_weight()))
            v = v.get_next()

    g_scc = Graph(nodes, edges)
    return g_scc