class Node:
    """
    This class represents points on two-dimentional cartesian axis system.
    """

    def __init__(self, name: str, neighbors: list, x: float, y: float):
        self.__name = name
        self.__neighbors = neighbors
        self.__x = x
        self.__y = y
    
    def get_name(self):
        """
        Returns:
            str: the name of the point.
        """
        return self.__name
    
    def get_neighbors(self):
        """
        Returns:
            list: list of neighbors accessible from the point.
        """
        return self.__neighbors
    
    def get_x(self):
        """
        Returns:
            float: the location of the point on the x-axis.
        """
        return self.__x
    
    def get_y(self):
        """
        Returns:
            float: the location of the point on the y-axis.
        """
        return self.__y

