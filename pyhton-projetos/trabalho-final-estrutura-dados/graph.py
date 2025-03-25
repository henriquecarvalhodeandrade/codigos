class Graph:
    def __init__(self, node):
        self.node = node
        self.edges = {node: {}}

    def addNode(self, new_node):
        if new_node in self.edges[self.node]:
            self.edges[self.node][new_node] += 1
        else:
            self.edges[self.node][new_node] = 1

    def deleteNode(self, node):
        if node not in self.edges[self.node]:
            return
        self.edges[self.node][node] -= 1

    def display(self):
        print("Localizações dos clientes")
        for node, conexoes in self.edges.items():
            for destino, peso in conexoes.items():
                print(f"{destino} -- ({peso})")