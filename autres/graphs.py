"""graphs class, maybe it will be usefull one day"""


from typing import Union, List


class Node(object):
    """Node class"""

    def __init__(self, name: str) -> None:
        """Node constructor"""
        self.name = name
        self.neighbors = []

    def __repr__(self) -> str:
        """string representation"""
        return f"'{self.name}' -> {[i.name for i in self.neighbors]}"

    def __add__(self, other: "Node") -> "Node":
        """add two nodes"""
        if other not in self.neighbors:
            self.neighbors.append(other)
        if self not in other.neighbors:
            other.neighbors.append(self)
        return self

    def __sub__(self, other: "Node") -> "Node":
        """remove a node from neighbors"""
        if other in self.neighbors:
            self.neighbors.remove(other)
        if self in other.neighbors:
            other.neighbors.remove(self)
        return self

    def __gt__(self, other: "Node") -> "Node":
        """add a neighbor to self"""
        if other not in self.neighbors:
            self.neighbors.append(other)
        return self

    def __lt__(self, other: "Node") -> "Node":
        """add a node from neighbors"""
        if self not in other.neighbors:
            other.neighbors.append(self)

    def __contains__(self, other: "Node") -> bool:
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

    def __init__(self,) -> None:
        """Graph constructor"""
        self.nodes = []
        self.distances = []

    def __add__(self, other: Union[Node, "Graph"]) -> "Graph":
        """add a node to the graph"""
        if isinstance(other, Node) and other not in self:
            self.nodes.append(other)
            self.distances.append([0 for _ in self.distances])
            for i in self.distances:
                i.append(0)
        else:
            for node in other:
                if node not in self:
                    self.nodes.append(node)
                    self.distances.append([0 for _ in self.distances])
                    for i in self.distances:
                        i.append(0)
        return self

    def __contains__(self, node: Node) -> bool:
        """check if a node is in the graph"""
        return node in self.nodes

    def __str__(self) -> str:
        """string representation"""
        return "["+", ".join([str(i) for i in self])+"]"

    def __iter__(self) -> List["Node"]:
        """iterate over nodes"""
        for i in self.nodes:
            yield i

    def __len__(self) -> int:
        """return the number of nodes"""
        return len(self.nodes)

    def path(self, start: Node, end: Node, _lenght: int = 0, path: List[Node] = []) -> List[Node]:
        """return the shortest path between two nodes"""
        if start == end:
            return path
        if _lenght >= len(self):
            return None
        l=[]
        for i in start:
            if i not in path:
                path.append(i)
                t=self.diskjstra(i, end, _lenght+1, path)
                print(t)
                if t!=[] and t is not None:
                    l.append(t)
                path.pop()
        if l!=[]:
            return min(l,key=len)
        return None

if __name__ == "__main__":
    graph = Graph()
    node1 = Node("node1")
    node2 = Node("node2")
    node3 = Node("node3")
    node4 = Node("node4")
    node5 = Node("node5")
    node6 = Node("node6")
    node7 = Node("node7")
    node8 = Node("node8")
    node9 = Node("node9")
    node10 = Node("node10")
    node11 = Node("node11")
    node12 = Node("node12")
    graph+node1+node2+node3+node4+node5+node6+node7+node8+node9+node10+node11+node12
    node2+node4+node1 > node5
    node4+node1 > node6
    node8 > node1+node2+node3+node4
    node9 > node1+node2 > node3 > node4
    node3 > node2
    node12+node9 < node5
    print(graph)
    print(graph.path(node1, node9))
