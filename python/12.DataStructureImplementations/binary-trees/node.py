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


RED = False
BLACK = True
class RBNode (Node):
    def __init__(self, value):
        super().__init__(value)
        self.color:bool = RED # defaults to red (false)