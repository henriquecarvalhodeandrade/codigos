from item import Item

class node:
    """Classe de um nó"""
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class linked_list:
    """Classe representando uma lista"""
    def __init__(self):
        self.head = node()

    """Método utilizado para adicionar algo à lista"""
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    """Método para remover algum valor pelo index"""
    def erase(self, index):
        if index < 0 or index >= self.lenght():
            print('ERROR! Index out of range')
            return
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1

    """Remove o primeiro nó encontrado que contém o valor especificado."""
    def remove_code(self, codigo):
        cur_node = self.head
        while cur_node.next is not None:
            last_node = cur_node
            cur_node = cur_node.next
            if isinstance(cur_node.data, Item) and cur_node.data.codigo == codigo:
                last_node.next = cur_node.next
                print(f"Código {codigo} removido.")
                return True
        print(f"Código {codigo} não encontrado no banco de dados.")
        return False
    
    """Método que retorna o tamanho da lista"""
    def lenght(self):
        cur = self.head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        print(count)
        return
    
    """Método que exibe os elementos em forma de lista"""
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        for i in elems:
            print(i)

    """Método para obter algum valor pelo index"""
    def get(self,index):
        if index < 0 or index >= self.lenght():
            print('ERROR! Index out of range')
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                print(cur_node.data)
                return
            cur_index += 1

    def get_list(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        return elems