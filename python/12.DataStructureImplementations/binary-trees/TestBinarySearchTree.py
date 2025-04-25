import unittest
from binary_search_tree import BinarySearchTree


"""
Testing skeleton code from ChatGPT
"""
class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        for val in [5, 3, 2, 1, 4, 7, 6, 9, 8, 10]:
            self.tree.insert(val)

    def test_max(self):
        self.assertEqual(self.tree.max(), 10)

    def test_min(self):
        self.assertEqual(self.tree.min(), 1)

    def test_find_predecessor(self):
        self.assertEqual(self.tree.find_predecessor(7), 6)

    def test_find_successor(self):
        self.assertEqual(self.tree.find_successor(7), 8)

    def test_inorder(self):
        self.assertEqual(self.tree.inorder(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_preorder(self):
        self.assertEqual(self.tree.preorder(), [5, 3, 2, 1, 4, 7, 6, 9, 8, 10])

    def test_postorder(self):
        self.assertEqual(self.tree.postorder(), [1, 2, 4, 3, 6, 8, 10, 9, 7, 5])

    def test_delete_leaf(self):
        self.tree.delete(10)  # leaf
        self.assertEqual(self.tree.inorder(), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_delete_one_child(self):
        self.tree.delete(9)  # one child (10)
        self.assertEqual(self.tree.inorder(), [1, 2, 3, 4, 5, 6, 7, 8, 10])

    def test_delete_two_children(self):
        self.tree.delete(5)  # root with two children
        self.assertEqual(self.tree.inorder(), [1, 2, 3, 4, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()
