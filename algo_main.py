import algo_module as ag
from graph import Graph
import poi_module as poi
import pandas as pd


def create_data_frame():
    # empty graph
    nodes_e = {
        "name" : [],
        "x" : [],
        "y" : []
    }
    edges_e = []
    # single node
    nodes_s = {
        "name" : [1],
        "x" : [1],
        "y" : [1]
    }
    edges_s = []
    # small graphs
    nodes1 = {
        "name" : [1, 2, 3, 4, 5, 6],
        "x" : [1, 2, 3, 4, 5, 6],
        "y" : [1, 2, 3, 4, 5, 6]
    }
    edges1 = [(1, 2, 1), (1, 4, 1), (2, 5, 1), (3, 5, 1), (3, 6, 1), (4, 2, 1), (4, 5, 1), (5, 4, 1)]
    nodes2 = {
        "name" : [1, 2, 3, 4, 5, 6, 7],
        "x" : [1, 2, 3, 4, 5, 6, 7],
        "y" : [1, 2, 3, 4, 5, 6, 7]
    }
    edges2 = [(1, 2, 1), (1, 3, 1), (1, 5, 1), (2, 6, 1), (3, 4, 1), (4, 5, 1),
              (4, 6, 1), (4, 7, 1), (5, 3, 1), (5, 7, 1), (6, 1, 1), (6, 7, 1)]
    return pd.DataFrame(nodes1), edges1


def print_graph(g):
    print("graph:")
    for node in g.get_nodes():
        print(node.get_name(), " --> ", [neighbor[0].get_name() for neighbor in node.get_neighbors()])


def print_bfs_res(dist, bfs_tree):
    print("### distances for source ###")
    for node in dist:
        print("distance of node ", node.get_name(), " is ", dist[node])
    print("### bfs tree ###")
    for node in bfs_tree:
        if bfs_tree[node] is None:
            print("node ", node.get_name(), " is root.")
        else:
            print("parent of node ", node.get_name(), " is ", bfs_tree[node].get_name())


def print_dfs_res(discovery_times, finish_times, dfs_forest):
    print("### discovery times ###")
    for node in discovery_times:
        print("discovery time of node ", node.get_name(), " is ", discovery_times[node])
    print("### finish times ###")
    for node in finish_times:
        print("finish time of node ", node.get_name(), " is ", finish_times[node])
    print("### dfs forest ###")
    for node in dfs_forest:
        if dfs_forest[node] is None:
            print("node ", node.get_name(), " is root.")
        else:
            print("parent of node ", node.get_name(), " is ", dfs_forest[node].get_name())


def main():
    # df = poi.get_data()
    # g = Graph(df, None)
    nodes, edges = create_data_frame()
    g = Graph(nodes, edges)
    print_graph(g)
    if g.get_size() > 0:
        s = 0
        dist, bfs_tree = ag.bfs(g, s)
        # print_bfs_res(dist, bfs_tree)
        discovery_times, finish_times, dfs_forest = ag.dfs(g)
        print_dfs_res(discovery_times, finish_times, dfs_forest)


if __name__ == "__main__":
    main()
