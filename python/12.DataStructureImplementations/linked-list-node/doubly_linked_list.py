from node import Node

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node

    def print_list(self):
        current = self.head
        while current.next:
            print(current.value, "-> ", end="")
            current = current.next
        print(current.value)
        return