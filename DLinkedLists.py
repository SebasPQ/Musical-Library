class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
        self.end_node = None

    # Métodos de la lista doblemente enlazada
    insert_in_emptylist = insert_in_emptylist

    insert_at_start = insert_at_start

    insert_at_end = insert_at_end

    insert_after_item = insert_after_item

    insert_before_item = insert_before_item

    delete_element_by_value = delete_element_by_value

    delete_at_start = delete_at_start

    delete_at_end = delete_at_end

    reverse_linked_list = reverse_linked_list

    traverse_list = traverse_list


def insert_in_emptylist(self, data):
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
        print("The list has no element to delete")
        return

    aux = self.start_node.nref

    if self.start_node == x:
        aux = self.start_node
        self.start_node = self.start_node.nref
        self.start_node.pref = None
        aux.nref = None
        return
    elif self.end_node == x:
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
                aux = None
                return
            aux1 = aux
            aux = aux.nref
            return

    print("Item not found")
    return


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
