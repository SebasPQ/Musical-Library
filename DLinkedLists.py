class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.any_node = None
    # Métodos de la lista doblemente enlazada

    def insert_in_empty_list(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            self.end_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            self.end_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            self.end_node = new_node
            return
        new_node = Node(data)
        new_node.pref = self.end_node
        self.end_node.nref = new_node
        self.end_node = new_node

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no elements to delete")
            return

        aux = self.start_node.nref
        if aux is None:
            self.start_node = None
        elif self.start_node.item == x:
            aux = self.start_node
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            aux.nref = None
            return
        elif self.end_node.item == x:
            aux = self.end_node
            self.end_node = self.end_node.pref
            self.end_node.nref = None
            aux.pref = None
            return
        else:
            while aux is not None:
                if aux.item == x:
                    aux.nref.pref = aux.pref
                    aux.pref.nref = aux.nref
                    aux.pref, aux.nref = None, None
                    return
                aux = aux.nref
            print("Item not found")
            return

    def delete_by_node(self, node):
        self.any_node = node
        if self.any_node.pref is None:
            self.delete_at_start()
        elif self.any_node.nref is None:
            self.delete_at_end()
        else:
            self.any_node.nref.pref = self.any_node.pref
            self.any_node.pref.nref = self.any_node.nref
            self.any_node.nref, self.any_node.pref = None, None
            self.any_node = None

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            self.end_node = None
            return
        self.start_node = self.start_node.nref
        self.start_node.pref = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            self.end_node = None
            return
        self.end_node = self.end_node.pref
        self.end_node.nref = None

    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to reverse")
            return
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref