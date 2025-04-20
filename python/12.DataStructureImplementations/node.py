"""
custom node class for use in making singly and doubly linked lists
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # points to next node
        self.prev = None # points to prev node

    def __repr__(self):
        return str({self.value})