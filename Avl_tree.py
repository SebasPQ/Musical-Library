import sys

from DLinkedLists import DoublyLinkedList


class BNode:
    def __init__(self, data):
        self.data = data
        self.content = DoublyLinkedList()
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0


class AVLTree:

    def __init__(self):
        self.root = None
        self.any = None

    def __print_helper(self, curr_ptr, indent, last):
        # print the tree structure on the screen
        if curr_ptr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(curr_ptr.data)

            self.__print_helper(curr_ptr.left, indent, False)
            self.__print_helper(curr_ptr.right, indent, True)

    def __search_tree_helper(self, node, key):
        if node is None or key == node.data:
            return node

        if key < node.data:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)

    def __delete_node_helper(self, node, key):
        # search the key
        if node is None:
            return node
        elif key < node.data:
            node.left = self.__delete_node_helper(node.left, key)
        elif key > node.data:
            node.right = self.__delete_node_helper(node.right, key)
        else:
            # the key has been found, now delete it
            # case 1: node is a leaf node
            if node.left is None and node.right is None:
                node = None

            # case 2: node has only one child
            elif node.left is None:
                node = node.right

            elif node.right is None:
                node = node.left

            # case 3: has both children
            else:
                temp = self.minimum(node.right)
                node.data = temp.data
                node.right = self.__delete_node_helper(node.right, temp.data)

        return node

    # update the balance factor the node
    def __update_balance(self, node):
        if node.bf < -1 or node.bf > 1:
            self.__rebalance(node)
            return

        if node.parent is not None:
            if node == node.parent.left:
                node.parent.bf -= 1

            if node == node.parent.right:
                node.parent.bf += 1

            if node.parent.bf != 0:
                self.__update_balance(node.parent)

    # rebalance the tree
    def __rebalance(self, node):
        if node.bf > 0:
            if node.right.bf < 0:
                self.right_rotate(node.right)
                self.left_rotate(node)
            else:
                self.left_rotate(node)
        elif node.bf < 0:
            if node.left.bf > 0:
                self.left_rotate(node.left)
                self.right_rotate(node)
            else:
                self.right_rotate(node)

    def __preorder_helper(self, node):
        if node is not None:
            sys.stdout.write(node.data + " ")
            self.__preorder_helper(node.left)
            self.__preorder_helper(node.right)

    def __inorder_helper(self, node):
        if node is not None:
            self.__inorder_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__inorder_helper(node.right)

    def __postorder_helper(self, node, std=None):
        if node is not None:
            self.__postorder_helper(node.left)
            self.__postorder_helper(node.right)
            std.out.write(node.data + " ")

    # Pre-Order traversal
    # Node->Left Subtree->Right Subtree
    def preorder(self):
        self.__preorder_helper(self.root)

    # In-Order traversal
    # Left Subtree -> Node -> Right Subtree
    def __inorder(self):
        self.__inorder_helper(self.root)

    # Post-Order traversal
    # Left Subtree -> Right Subtree -> Node
    def __postorder(self):
        self.__postorder_helper(self.root)

    # search the tree for the key k
    # and return the corresponding node
    def search_tree(self, k):
        return self.__search_tree_helper(self.root, k)

    # find the node with the minimum key
    @staticmethod
    def minimum(node):
        while node.left is not None:
            node = node.left
        return node

    # find the node with the maximum key
    @staticmethod
    def maximum(node):
        while node.right is not None:
            node = node.right
        return node

    # find the successor of a given node
    def successor(self, x):
        # if the right subtree is not null,
        # the successor is the leftmost node in the
        # right subtree
        if x.right is not None:
            return self.minimum(x.right)

        # else it is the lowest ancestor of x whose
        # left child is also an ancestor of x.
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    # find the predecessor of a given node
    def predecessor(self, x):
        # if the left subtree is not null,
        # the predecessor is the rightmost node in the
        # left subtree
        if x.left is not None:
            return self.maximum(x.left)

        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    # rotate left at node x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

        # update the balance factor
        x.bf = x.bf - 1 - max(0, y.bf)
        y.bf = y.bf - 1 + min(0, x.bf)

    # rotate right at node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

        # update the balance factor
        x.bf = x.bf + 1 - min(0, y.bf)
        y.bf = y.bf + 1 + max(0, x.bf)

    # insert the key to the tree in its appropriate position
    def insert(self, key, index):
        # Verifies if node already exists
        node = self.search_tree(key.item[index].lower())
        if node is not None:
            node.content.insert_at_end(key)
        else:
            # PART 1: Ordinary BST insert
            node = BNode(key.item[index].lower())
            node.content.insert_at_end(key)
            y = None
            x = self.root

            while x is not None:
                y = x
                if node.data < x.data:
                    x = x.left
                else:
                    x = x.right

            # y is parent of x
            node.parent = y
            if y is None:
                self.root = node
            elif node.data < y.data:
                y.left = node
            else:
                y.right = node
        # PART 2: re-balance the node if necessary
        self.__update_balance(node)

    # delete the node from the tree
    def delete_node(self, data):
        return self.__delete_node_helper(self.root, data)

    def delete_by_node(self, node):
        self.any = node

        if self.any.left is None and self.any.right is None:
            if self.any.parent.right == self.any:
                self.any.parent.right = None
                self.any = None
            else:
                self.any.parent.left = None
                self.any = None
        # case 2: node has only one child
        elif self.any.left is None:
            self.any.parent.right = self.any.right
            self.any.right.parent = self.any.parent
            self.any = None

        elif self.any.right is None:
            self.any.parent.left = self.any.left
            self.any.left.parent = self.any.parent
            self.any = None

        # case 3: has both children
        else:
            temp = self.minimum(self.any.right)
            self.any.data = temp.data
            self.any.right = self.__delete_node_helper(self.any.right, temp.data)

        return self.any

    # print the tree structure on the screen
    def print_tree(self):
        self.__print_helper(self.root, "", True)
