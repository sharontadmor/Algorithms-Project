import algo_module as ag
from graph import Graph
import poi_module as poi
import pandas as pd


def edges_from_df(df: pd.DataFrame):
    """
    
    Args:
        df (pd.DataFrame).

    Returns:
        edges (list): list of tuples (n, m, w), where there's an edge from n to m with weight w.
    """
    edges = []
    for i in range(df.shape[0]):
        edge = df.apply(create_edge, axis=1, args=(i, df)).dropna().tolist()
        edges.extend(edge)
    return edges

def create_edge(row: pd.Series, idx: int, df: pd.DataFrame):
    """_summary_

    Args:
        row (pandas series): first pandas series.
        idx (int): index of second pandas series.
        df (DataFrame): data frame containing given series.

    Returns:
        tuple (i, j, v), where i and j are indexes and v is value calculated.
    """
    if idx != row.name:
        return (idx, row.name, dist(df.iloc[idx], row))

def dist(row1: pd.Series, row2: pd.Series):
    """
    Args:
        row1 (pandas Series): DataFrame row.
        row2 (pandas Series): DataFrame row.

    Returns:
        float: Euclidean distance between two nodes.
    """
    return (((row2['x'] - row1['x']) ** 2) + ((row2['y'] - row1['y']) ** 2)) ** 0.5

def nodes_from_df(df: pd.DataFrame):
    """
    each node in a graph correspond to the number of row in a data frame.

    Args:
        df (pd.DataFrame).

    Returns:
        list: list of nodes.
    """
    size = df.shape[0]
    return [i for i in range(size)]

def poi_from_graph(node: int, df: pd.DataFrame):
    """
    each node in a graph correspond to the number of row in a data frame.

    Args:
        node (int): index of node in a graph.
        df (pd.DataFrame): given data frame.

    Returns:
        pd.Series: record represented by given node.
    """
    return df.iloc[node]

def main():
    df = poi.get_data()
    nodes = nodes_from_df(df)
    edges = edges_from_df(df)
    g = Graph(nodes, edges)
    # print_graph(g)
    # if g.get_size() > 0:
    #     s = 0
    #     dist, bfs_tree = ag.bfs(g, s)
    #     # print_bfs_res(dist, bfs_tree)
    #     discovery_times, finish_times, dfs_forest = ag.dfs(g)
    #     print_dfs_res(discovery_times, finish_times, dfs_forest)
    # ag.strongly_connected_components(g)


if __name__ == "__main__":
    main()
