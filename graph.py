from node import Node
import numpy as np
import pandas as pd


class Graph:
    """
    This class represents a directed weighed graph,
    whose nodes are points on two-dimentional cartesian axis system.
    Graph representation method is adjacency list.
    """
    def __init__(self, nodes: pd.DataFrame, edges: list):
        self.__size = nodes.shape[0]
        self.__nodes = []
        self.__set_nodes(nodes)
        self.__set_adjacencies(edges)
        """
        This class represents a full weighed graph.
        Graph representation method is adjacency matrix.
        """
        """
        # numpy array of dim 1, values initialized to nan.
        self.__nodes = []
        self.__set_nodes(df)
        # numpy array of dim 2, values initialized to nan.
        self.__adjacencies = np.full([self.__size, self.__size], np.nan)
        self.__set_adjacencies()
        """

    def get_size(self):
        """
        Returns:
            number of nodes in the graph.
        """
        return self.__size

    def get_nodes(self):
        """
        Returns:
            a list containing Node objects.
        """
        return self.__nodes

    def __set_nodes(self, df: pd.DataFrame):
        """
        sets the nodes of the graph as the points given in df.
        Args:
            df (pd.DataFrame): a pandas data frame containing the names of poi (points of interest) and their datum-points.
        """
        # create pandas Series where each element is a Node object, than convert to list:
        self.__nodes = df.apply(self.create_node, axis=1).tolist()

    def create_node(self, row: pd.Series):
        """
        Args:
            row (pandas Series): DataFrame row.
        Returns:
            Node: a Node object.
        """
        return Node(row["name"], [], row["x"], row["y"])

    def __set_adjacencies(self, edges: list):
        """
        adds edges to graph.
        if edges list is None, sets the graph to be a full graph,
        with the weight of each edge as the distance between two nodes.
        else, sets the edges with weights specified in edges list.

        Args:
            edges (list): list of tuples (n, m, w), where there's an edge from n to m with weight w.
            None if the graph is a full graph. 
        """
        if not edges:
            for i in range(self.get_size()):
                n = self.get_nodes()[i]
                for j in range(self.get_size()):
                    if i != j:
                        m = self.get_nodes()[j]
                        n.get_neighbors().append((m, self.dist(n, m)))
            return
        for edge in edges:
            for i in range(self.get_size()):
                n = self.get_nodes()[i]
                if n.get_name() == edge[0]:
                    for j in range(self.get_size()):
                        m = self.get_nodes()[j]
                        if m.get_name() == edge[1]:
                            n.get_neighbors().append((m, edge[2]))

    def dist(self, node1: Node, node2: Node):
        """
        Args:
            node1 (Node):  a Node object.
            node2 (Node):  a Node object.

        Returns:
            float: Euclidean distance between two nodes.
        """
        x1 = node1.get_x()
        x2 = node2.get_x()
        y1 = node1.get_y()
        y2 = node2.get_y()
        return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
