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

    def _create_node(self, value) -> AVLNode:
        return AVLNode(value)

    def __init__(self):
        super().__init__()


    def insert(self, value):
        inserted_node = super().insert(value)
        self._rebalance_upward(inserted_node)

    def _rebalance_upward(self, node):
        while node: # go through all the parents up to root
            node.update_height()
            balance = node.balance_factor()
            # left heavy
            if balance > 1:
                if node.left and node.left.balance_factor() < 0: # left-right ... node.left has heavy right...
                    self.rotate_left(node.left)
                self.rotate_right(node)
            # right heavy
            elif balance < -1:
                if node.right and node.right.balance_factor() > 0:
                    self.rotate_right(node.right)
                self.rotate_left(node)
            node = node.parent

    def rotate_left(self, node):
        a = node
        b = node.right
        if not b:
            return
        a.right = b.left
        if b.left:
            b.left.parent = a
        if not a.parent: # root
            self.root = b
            b.parent = None
        else:
            # connect a.parent to b
            if a.parent.left is a:
                a.parent.left = b
            else:
                a.parent.right = b
        b.parent = a.parent
        a.parent = b
        b.left = a
        a.update_height()
        b.update_height()


    def rotate_right(self, node):
        c = node
        b = node.left
        if not b:
            return
        c.left = b.right
        if b.right:
            b.right.parent = c
        if not c.parent: # root
            self.root = b
            b.parent = None
        else:
            if c.parent.left is c:
                c.parent.left = b
            else:
                c.parent.right = b
        b.parent = c.parent
        c.parent = b
        b.right = c
        b.update_height()
        c.update_height()


    def delete(self, value):
        node = self.search(value)
        if node:
            self._delete_node(node)

    def _delete_node(self, node):
        if node.left and node.right: # two children
            successor = self.find_successor(node)
            node.value = successor.value
            node = successor

        replacement = node.left if node.left else node.right

        if replacement:
            replacement.parent = node.parent
            if not node.parent:
                self.root = replacement
            else:
                if node.parent.left == node:
                    node.parent.left = replacement
                else:
                    node.parent.right = replacement
            self._rebalance_upward(replacement.parent)
        else:
            if not node.parent:
                self.root = None
            else:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
                self._rebalance_upward(node.parent)



if __name__ == '__main__':
    tree = AVL_tree()
    tree.insert(2)
    tree.insert(3)
    tree.insert(5)
    tree.print_tree()