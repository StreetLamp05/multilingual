import unittest
from AVL_tree import AVL_tree  # Assuming your AVL tree is in avl_tree.py


class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.tree = AVL_tree()

    def test_insert_balances(self):
        for val in [10, 20, 30, 40, 50, 25]:
            self.tree.insert(val)

        # After inserting values that should cause rotations, check balance
        self.assertTrue(self.is_balanced(self.tree.root))
        self.assertEqual(self.tree.inorder(), [10, 20, 25, 30, 40, 50])

    def test_delete_balances(self):
        for val in [10, 20, 30, 40, 50, 25]:
            self.tree.insert(val)

        self.tree.delete(50)
        self.tree.delete(40)

        self.assertTrue(self.is_balanced(self.tree.root))
        self.assertEqual(self.tree.inorder(), [10, 20, 25, 30])

    def test_min_max(self):
        for val in [15, 10, 20, 8, 12, 17, 25]:
            self.tree.insert(val)

        self.assertEqual(self.tree.min(), 8)
        self.assertEqual(self.tree.max(), 25)

    def test_search(self):
        for val in [5, 15, 25]:
            self.tree.insert(val)

        self.assertIsNotNone(self.tree.search(15))
        self.assertIsNone(self.tree.search(100))

    def test_preorder(self):
        for val in [30, 20, 40, 10, 25, 35, 50]:
            self.tree.insert(val)

        # Preorder: Root, Left, Right
        self.assertEqual(self.tree.preorder(), [30, 20, 10, 25, 40, 35, 50])

    def is_balanced(self, node):
        """
        Helper function to verify that the AVL tree is balanced.
        """
        if node is None:
            return True

        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0

        if abs(left_height - right_height) > 1:
            return False

        return self.is_balanced(node.left) and self.is_balanced(node.right)


if __name__ == '__main__':
    unittest.main()
