from node import AVLNode
from binary_search_tree import BinarySearchTree

class AVL_tree(BinarySearchTree):
    """
    Subclass of BinarySearchTree that implements AVL methods.
    Keeping:
    search(), inorder(), preorder(), postorder(), min(), max(),
    print_tree(), find_predecessor(), find_successor()

    Overriding/ Extending:
    insert(), delete()

    Adding:
    rotate_left(), rotate_right()
    """
    def __init__(self):
        super().__init__()


    def insert(self, value):
        inserted_node = super().insert(value)
        inserted_node._rebalance_upward(inserted_node)

    def _rebalance_upward(self, node):
        while node: # go through all the parents up to root
            node.update_height()
            balance = node.balance_factor
            # left heavy
            if balance > 1:
                if node.left and node.left.balance_factor() < 0: # left-right ... node.left has heavy right...
                    self.rotate_left(node.left)
                self.rotate_right(node)
            # right heavy
            elif balance < -1:
                if node.right and node.right.balance_factor() > 0:
                    self.rotate_right(node.right)
                self.rotate_left(node.right)
            node = node.parent

    def rotate_left(self, node):
        if node.parent is self.root:
            parent = node.parent
            self.root = node
            node.parent = None
            node.left = parent
            parent.parent = node
        else:
            grandparent = node.parent.parent
            parent = node.parent
            if grandparent.left == parent: # left of grandparent
                grandparent.left = node
                node.parent = grandparent
                node.left = parent
                parent.parent = node
            elif grandparent.right == parent: # right of grandparent
                grandparent.right = node
                node.parent = grandparent
                node.right = parent
                parent.parent = node

    def rotate_right(self, node):
        if node.parent is self.root:
            parent = node.parent
            self.root = node
            node.parent = None
            node.right = parent
            parent.parent = node
        else:
            grandparent = node.parent.parent
            parent = node.parent
            if grandparent.left is parent:
                grandparent.left = node
                node.parent = grandparent
                node.right = parent
                parent.parent = node
            elif grandparent.right is parent:
                grandparent.right = node
                node.parent = grandparent
                node.right = parent
                parent.parent = node
