from Node import Node
from typing import List


class Lista:
    def __init__(self, *nodes: Node):
        self.data: Node = nodes

    @classmethod
    def build_from_list_of_nodes(cls, nodes: List[Node]):
        return Lista(*nodes)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        # no puede ser <= porque si no iterará una posición de mas siempre
        if self.value < len(self.data):
            self.value += 1
            return self[self.value - 1]
        else:
            raise StopIteration

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Lista.build_from_list_of_nodes(
                [self[ii] for ii in range(*index.indices(len(self)))]
            )
        if isinstance(index, int):
            if index < 0:
                return self.data[len(self) + index]
            elif index >= 0 and index < len(self):
                return self.data[index]

    def __len__(self):
        return len(self.data)

    def __str__(self) -> str:
        string = ""
        for v in self.data:
            string += str(v) + " | "
        return string


lista = Lista(Node(20), Node(30), Node(40))
assert len(lista) == 3
assert lista[:2][0].value == 20 and isinstance(lista[:2][0], Node)
assert lista[:2][1].value == 30 and isinstance(lista[:2][1], Node)
assert lista[-1].value == 40 and isinstance(lista[-1], Node)
