from node import Node
import numpy as np
import pandas as pd


class Graph:
    """
    This class represents a full directed graph or an undirected graph.
    adjacency relations between nodes are represented by a weighed adjacency matrix,
    which is implemented with numpy.
    """

    def __init__(self, df: pd.DataFrame):
        self.__size = df.shape[0]
        # numpy array of dim 1, values initialized to nan.
        self.__nodes = np.full(self.__size, np.nan)
        self.__set_nodes(df)
        # numpy array of dim 2, values initialized to nan.
        self.__adjacencies = np.full([self.__size, self.__size], np.nan)
        self.__set_adjacencies()

    def get_nodes(self):
        """
        Returns:
            ndarray: a numpy array containing Node objects.
        """
        return self.__nodes

    def __set_nodes(self, df: pd.DataFrame):
        """
        sets the nodes of the graph as the points given in df.
        Args:
            df (pd.DataFrame): a pandas data frame containing the names of poi (points of interest) and their datum-points.
        """
        pass

    def __set_adjacencies(self):
        pass

    def calc_dist(node1: Node, node2: Node):
        pass