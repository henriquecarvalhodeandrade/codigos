class NodeTree():
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None
    
    def insert(self, node, id, data):
        if self.root is None:
            self.root = NodeTree(id, data)
        else:
            if id < node.id:
                if node.left is None:
                    node.left = NodeTree(id, data)
                else:
                    self.insert(node.left, id)
            if id > node.id:
                if node.right is None:
                    node.right = NodeTree(id, data)
                else:
                    self.insert(node.right, id) 

    def search(self, node, id):
        if node is None:
            return False  # ID não encontrado
        if node.id == id:
            return True  # ID encontrado
        if id < node.id:
            return self.search(node.left, id)
        return self.search(node.right, id)
    
    def getNode(self, node, id):
        if node is None or node.id == id:
            return node.data
        if id < node.id:
            return self.getNode(node.left, id)
        return self.getNode(node.right, id)


    
    def printInOrder(self, node):
        if self.isEmpty():
            print("Empty Tree!")
        else:
            if node.left:
                self.printInOrder(node.left)
            print(f"{node.id} - {node.data}")
            if node.right:
                self.printInOrder(node.right)
    
    def countNodes(self, node):
        if self.isEmpty():
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)
    
    def delete(self, node, id):
        if node is None:
            return node
        if id < node.id:
            node.left = self.delete(node.left, id) #Função Recursiva
        elif id > node.id:
            node.right = self.delete(node.right, id) #Função Recursiva
        else:
            #Case 1: The node to be deleted has no children (leaf node)
            if node.left is None and node.right is None:
                return None
            #Case 2: The node to be deleted has only one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            #Case 3: The node to be deleted has two children
            else:
                #Find sucessor (smallest value of right subtree)
                sucessor = self._minValueRight(node.right)
                node.id = sucessor.id
                #Delete the sucessor
                node.right = self.delete(node.right, sucessor.id)
        
        return node

    def deleteTree(self):
        self.root = None