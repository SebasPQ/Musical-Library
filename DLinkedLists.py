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
    insert_in_emptylist=insert_in_emptylist

    insert_at_start=insert_at_start

    insert_at_end=insert_at_end

    insert_after_item=insert_after_item

    insert_before_item=insert_before_item

    delete_element_by_value=delete_element_by_value

    delete_at_start=delete_at_start

    delete_at_end=delete_at_end

    reverse_linked_list=reverse_linked_list

    traverse_list=traverse_list


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

