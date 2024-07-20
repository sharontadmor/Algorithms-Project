from graph import Graph

NODE = 0
HEAD_OF_QUEUE = 0


def bfs(g: Graph, idx: int) -> tuple[dict, dict]:
    """
    BFS algorithm.
    Args:
        g (Graph object): a Graph object.
        idx (int): index of source vertex.
    """
    s = g.get_nodes()[idx] 
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
        for i in range(len(u.get_neighbors())):
            v = u.get_neighbors()[i][NODE]
            if v not in visited:
                visited.append(v)
                dist[v] = dist[u] + 1
                bfs_tree[v] = u
                Q.append(v)
        Q.remove(u)
        visited.append(u)
    return dist, bfs_tree


def dfs(g: Graph):
    """
    DFS algorithm.
    Args:
        g (Graph object): a graph.
    """
    # set initial values
    time = 0
    visited = []
    discovery_times = {}
    finish_times = {}
    dfs_forest = {}
    # traverse graph
    for i in range(len(g.get_nodes())):
        if g.get_nodes()[i] not in visited:
            dfs_forest[g.get_nodes()[i]] = None
            time = dfs_visit(g, i, time, visited, discovery_times, finish_times, dfs_forest)
    return discovery_times, finish_times, dfs_forest


def dfs_visit(g: Graph, idx: int, time: int, visited: list, discovery_times: dict, finish_times: dict, dfs_forest: dict):
    """
    Args:
        g (Graph object): a Graph object.
        idx (int): index of source vertex.
    """
    u = g.get_nodes()[idx]
    time += 1
    discovery_times[u] = time
    visited.append(u)
    for i in range(len(u.get_neighbors())):
        v = u.get_neighbors()[i][NODE]
        if v not in visited:
            dfs_forest[v] = u
            time = dfs_visit(g, g.get_nodes().index(v), time, visited, discovery_times, finish_times, dfs_forest)
    time += 1
    finish_times[u] = time
    return time
    