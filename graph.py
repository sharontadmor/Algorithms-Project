class Graph:
    """
    This class represents a static directed weighed graph,
    Graph representation method is adjacency list.
    """
    def __init__(self, nodes: list[int], edges: list):
        self.__size = len(nodes)
        self.__nodes = nodes
        self.__adj_list = [None] * len(nodes)
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
    
    class Neighbor:
        """
        This class represents a node in a linked list.
        """

        def __init__(self, data: int, weight: float, next=None):
            self.__data = data
            self.__edge_weight = weight
            self.__next = next
        
        def get_data(self):
            """
            Returns:
                int: index of this node.
            """
            return self.__data
        
        def get_weight(self):
            """
            Returns:
                float: weight of edge.
            """
            return self.__edge_weight
        
        def get_next(self):
            """
            Returns:
                Neighbor: next node in the linked list.
            """
            return self.__next
        
        def set_next(self, node):
            """
            Args:
                node (Neighbor): next node in the linked list.
            """
            self.__next = node
    

    def get_size(self):
        """
        Returns:
            number of nodes in the graph.
        """
        return self.__size
    
    def get_nodes(self):
        """
        Returns:
            list[int]: list of nodes in this graph.
        """
        return self.__nodes
    
    def get_node(self, i: int):
        """
        Args:
            i (int): index of node in nodes list.

        Returns:
            int: name of node in index i in nodes list.
        """
        return self.__nodes[i]
    
    def get_adj_list(self):
        """
        linked list in the i'th cell is neighbors list of nodes j for each (i, j) is an edge.

        Returns:
            list: list of linked lists.
        """
        return self.__adj_list
    
    def get_adj_list_by_index(self, i: int):
        """
        linked list in the i'th cell is neighbors list of nodes j for each (i, j) is an edge.

        Args:
            i (int): index of node in nodes list.

        Returns:
            Neighbor: head of neighbors list.
        """
        return self.__adj_list[i]
    
    def get_adj_list_by_name(self, n: int):
        """
        linked list in the i'th cell is neighbors list of nodes j for each (i, j) is an edge.

        Args:
            n (int): name of node in nodes list.

        Returns:
            Neighbor: head of neighbors list.
        """
        idx = self.get_nodes().index(n)
        return self.__adj_list[idx]

    def __set_adjacencies(self, edges: list):
        """
        adds edges to graph.

        Args:
            edges (list): list of tuples (n, m, w), where there's an edge from n to m with weight w.
        """
        for edge in edges:
            self.add_edge(edge[0], edge[1], edge[2])
    
    def add_edge(self, s: int, t: int, w: float):
        """
        Args:
            s (int): name of source node.
            t (int): name of target node.
            w (float): weight of new edge.
        """
        idx = self.get_nodes().index(s)
        adj_list = self.get_adj_list_by_name(s)
        if not adj_list:
            # set first neighbor
            self.__adj_list[idx] = Graph.Neighbor(t, w)
        elif not self.edge(s, t, w):
            # add neighbor to end of linked list
            curr = adj_list
            while curr.get_next():
                curr = curr.get_next()
            curr.set_next(Graph.Neighbor(t, w))
    
    def edge(self, s: int, t: int, w: float):
        """
        Args:
            s (Node): name of source node.
            t (Node): name of target node.
            w (float): weight of new edge.

        Returns:
            boolean: True if there is an edge from s to t, False otherwise.
        """
        # nodes = self.get_adj_list()
        # if s < 0 or s >= len(nodes):  # Check if s is a valid index
        #     return False
        curr = self.get_adj_list_by_name(s)
        while curr:
            if curr.get_data() == t and curr.get_weight() == w:
                return True
            curr = curr.get_next()
        return False
    
    def in_deg(self, n: int):
        """
        Args:
            n (int): name of node.

        Returns:
            int: in degree of n.
        """
        in_deg = 0
        for i in range(self.get_size()):
            curr = self.get_adj_list_by_index(i)
            while curr:
                if curr.get_data() == n:
                    in_deg += 1
                curr = curr.get_next()
        return in_deg
    
    def out_deg(self, n: int):
        """
        Args:
            n (int): name of node.

        Returns:
            int: out degree of n.
        """
        out_deg = 0
        curr = self.get_adj_list_by_name(n)
        while curr:
            out_deg += 1
            curr = curr.get_next()
        return out_deg
    
