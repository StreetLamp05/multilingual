"""
Helper class to implement custom BSTs....
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class AVLNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1 # leaf node is 1, null/ nil is 0

    def update_height(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = 1 + max(left_height, right_height)

    def balance_factor(self) -> int:
        left = self.left.height if self.left else 0
        right = self.right.height if self.right else 0
        return left - right


RED = False
BLACK = True
class RBNode (Node):
    def __init__(self, value):
        super().__init__(value)
        self.color:bool = RED # defaults to red (false)