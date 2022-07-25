"""graphs class, maybe it will be usefull one day"""


from typing import Union, List

class Node(object):
    """Node class"""

    def __init__(self, name:str) -> None:
        """Node constructor"""
        self.name = name
        self.neighbors = []

    def __repr__(self) -> str:
        """string representation"""
        return f"'{self.name}' -> {[i.name for i in self.neighbors]}"

    def __add__(self, other:"Node") -> "Node":
        """add two nodes"""
        self.neighbors.append(other)
        other.neighbors.append(self)
        return self

    def __sub__(self, other:"Node") -> "Node":
        """remove a node from neighbors"""
        if other in self.neighbors:
            self.neighbors.remove(other)
        if self in other.neighbors:
            other.neighbors.remove(self)
        return self

    def __gt__(self, other:"Node") -> "Node":
        """add a neighbor to self"""
        self.neighbors.append(other)
        return self

    def __lt__(self, other:"Node") -> "Node":
        """add a node from neighbors"""
        other.neighbors.add(self)

    def __contains__(self, other:"Node") -> bool:
        """check if a node is in the neighbors"""
        return other in self.neighbors

    def __iter__(self) -> "Node":
        """iterate over neighbors"""
        for i in self.neighbors:
            yield i

    def __len__(self) -> int:
        """return the number of neighbors"""
        return len(self.neighbors)


class Graph(object):
    """Graph class"""

    def __init__(self) -> None:
        """Graph constructor"""
        self.nodes = []

    def __add__(self, node:Union[Node,"Graph"]) -> "Graph":
        """add a node to the graph"""
        if isinstance(node, Node):
            self.nodes.append(node)
        else:
            self.nodes.extend(node.nodes)
        return self

    def __str__(self) -> str:
        """string representation"""
        return "["+", ".join([str(i) for i in self])+"]"
    
    def __iter__(self) -> List["Node"]:
        """iterate over nodes"""
        for i in self.nodes:
            yield i


if __name__=="__main__":
    graph=Graph()
    node1=Node("node1")
    node2=Node("node2")
    node3=Node("node3")
    node4=Node("node4")
    graph+node1+node2+node3+node4
    node2+node4+node1
    node3>node2
    print(graph)
