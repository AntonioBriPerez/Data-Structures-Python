class Node:
    def __init__(self, value: int):
        self.value = value
        self.description = "Soy un nodo"

    def __str__(self):
        return f"Valor: {self.value} - Descr: {self.description}"
