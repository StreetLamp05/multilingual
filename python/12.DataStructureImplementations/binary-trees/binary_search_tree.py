from node import Node
from typing import Optional
import unittest


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def insert(self, value) -> None:
        """
        Insert a node into a BST, maintaining sorted order.
        :param value: The value to insert.
        :return: The inserted node (needed for subclass implementation).
        """
        if self.root is None:
            self.root = Node(value)
            self.size += 1
            return self.root
        else:
            return self.__recursive_insert(self.root, value)

    def __recursive_insert(self, node, value):
        """
        Recursively insert a node into a BST. Follows no duplicates rule
        :param node: The current node in the recursive traversal.
        :param value: The value to insert into the tree.
        :return: Node: The updated node reference after the insertion.
        """
        new_node = Node(value)
        if value < node.value: # look left
            if node.left:
                self.__recursive_insert(node.left, value)
            else:
                node.left = new_node
                new_node.parent= node

        elif value > node.value: # look right
            if node.right:
                self.__recursive_insert(node.right, value)
            else:
                node.right = new_node
                new_node.parent= node
        elif value == node.value: # ignore (no duplicates rule)
            return

    def delete(self, value) -> None:
        """
        Delete a node from a BST, maintaining sorted order. Uses inorder successor
        3 cases:
        1. Delete a leaf node -> just remove the node
        2. Delete a node w/ 1 child -> replace node w/ child value and remove child
        3. Delete a node w/ 2 children -> copy inorder successor/ predecessor into node and delete the predecessor/ successor
        :param value: The value to delete.
        :return: None
        """
        to_delete = self.search(value)
        if not to_delete:
            raise Exception(f"Value {value} not found.")
        self._delete(to_delete)
        self.size -= 1
        pass

    def _delete(self, node):
        # case 1: leaf node
        if node.left is None and node.right is None:
            if node == self.root: # delete root
                self.root = None
            else:
                parent = node.parent
                if parent.left == node:
                    parent.left = None
                else: parent.right = None
            node.parent = None

        # case 2: one child
        elif node.left is None or node.right is None:
            child = node.left if node.left else node.right
            if node == self.root: # deleting root node
                self.root = child
                child.parent = None
            else:
                parent = node.parent
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
                child.parent = parent
                node.parent = node.left = node.right = None

        # case 3: two children
        elif node.left and node.right:
            successor = self._successor(node)
            node.value = successor.value
            self._delete(successor)


    def search(self, value) -> Optional[Node]:
        """
        Search for a value in a BST.
        :param value: The value to search for
        :return: The Node with the value or None if it doesn't exist.
        """
        current = self.root
        while 1:
            if current.value == value:
                return current
            elif value < current.value:
                if current.left:
                    current = current.left
                elif current.value == value:
                    return current
                else: return None
            elif value > current.value:
                if current.right:
                    current = current.right
                elif current.value == value:
                    return current
                else: return None

    def inorder(self) -> list:
        """
        Returns a list of the tree in inorder traversal.
        Left, Root, Right
        Going to implement in 3 steps:
        1. Visit left child (if exists)
         - recursively call inorder to left subtree
        2. record current nodes value (after finishing left subtree)
        3. visit right child (if exists)
         - recursively call inorder to right subtree
        :return: list The inorder traversal.
        """
        def _inorder(node):
            if not node:
                return[]
            return _inorder(node.left) + [node.value] + _inorder(node.right)
        return _inorder(self.root)



    def preorder(self) -> list:
        """
        Returns a list of the tree in preorder traversal.
        Root, Left, Right
        Going to implement in 3 steps:
        1. Record Current Node's value
        2. Visit left child (if exists)
        3. Visit right child (if exists)
        :return: list The preorder traversal.
        """
        def _preorder(node):
            if not node:
                return []
            return [node.value] + _preorder(node.left) + _preorder(node.right)
        return _preorder(self.root)


    def postorder(self) -> list:
        """
        Returns a list of the tree in postorder traversal.
        Left, Right, Root
        Going to implement in 3 steps:
        Visit left child (if exists)
        Visit right child (if exists)
        Record current Node's value
        :return: list The postorder traversal.
        """
        def _postorder(node):
            if not node:
                return []
            return _postorder(node.left) + _postorder(node.right) + [node.value]
        return _postorder(self.root)


        return
    def min(self):
        """
        Returns the smallest value in the tree.
        :return: The smallest value in the tree.
        """
        current : Node = self.root
        while current.left:
            current = current.left
        return current.value

    def max(self):
        """
        Returns the largest value in the tree.
        :return: the largest value in the tree.
        """
        current : Node = self.root
        while current.right:
            current = current.right
        return current.value

    def find_predecessor(self, value):
        """
        Returns the predecessor of the given value.
        The predecessor is the largest node smaller than the given node.
        :param value: The value in the tree to find the predecessor of.
        :return: the predecessor of the given value.
        """
        toFind : Node = self.search(value)
        if toFind is None:
            raise Exception('Value not found')
        else:
            return self._predecessor(toFind).value

    def _predecessor(self, node: Node) -> Optional[Node]:
        """
        Returns the predecessor of the given node.
        :param node: The node to find the predecessor of.
        :return: the predecessor of the given node.
        """
        current = node
        current = current.left
        while current:
            if current.right:
                current = current.right
            elif current.left:
                current = current.left
            else:
                return current
        return None

    def find_successor(self, value):
        toFind : Node = self.search(value)
        if toFind is None:
            raise Exception('Value not found')
        else:
            return self._successor(toFind).value

    def _successor(self, node: Node) -> Optional[Node]:
        current = node
        current = current.right
        while current:
            if current.left:
                current = current.left
            elif current.right:
                current = current.right
            else:
                return current
        return None

    def print_tree(self, node=None, level=0, prefix="Root: "):
        """
        Recursively prints the tree sideways for visualization (this is from chatgpt lol)
        :param node: The starting node (default is self.root)
        :param level: Used for indentation based on depth
        :param prefix: Label for the current node
        """
        if node is None:
            node = self.root
        if node.right:
            self.print_tree(node.right, level + 1, "/---- ")
        print("     " * level + prefix + str(node.value))
        if node.left:
            self.print_tree(node.left, level + 1, "\\---- ")

if __name__ == '__main__':
    tree = BinarySearchTree()
    for val in [5, 3, 2, 1, 4, 7, 6, 9, 8, 10]:
        tree.insert(val)

    print(tree.preorder())
