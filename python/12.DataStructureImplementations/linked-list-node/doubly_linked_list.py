from node import Node

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_size(self):
        print(self.size)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.size:
            raise ValueError("Index out of range")
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else: # in middle
            i = 0
            current = self.head
            while i < index - 1:  # go before deleted node
                current = current.next
                i += 1
            # connect forward
            current.next.prev = new_node
            new_node.next = current.next
            # connect backward
            new_node.prev = current
            current.next = new_node
        self.size += 1


    def delete(self, instance):
        if instance < 0 or instance > self.size:
            raise Exception("Invalid index")
        elif instance == self.size - 1: # at tail
            self.tail = self.tail.prev
            self.tail.next.prev = None # clear deleted nodes pointers
            self.tail.next = None # set new tail next to null
        elif instance == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            i = 0
            current = self.head
            while i < instance - 1: # go before deleted node
                current = current .next
                i += 1
            current.next = current.next.next
            current.next.prev = current
        self.size -= 1
    """
    delete in middle, can make this more time efficient to O(n/2) by making it 
    so if deleted instance is in the first half, it will start at head and if 
    it is in second half, it will start from tail
    """

    def print_list(self):
        current = self.head
        while current.next:
            print(current.value, "<-> ", end="")
            current = current.next
        print(current.value)
        return
    """
    prints the backwards connections, to make sure prev pointers are correctly set
    """
    def print_backward(self):
        current = self.tail
        print("tail -> ", end="")
        while current:
            print(current.value, "<-> ", end="")
            current = current.prev

if __name__ == "__main__":
    myList = doubly_linked_list()
    myList.append(1)
    myList.append(2)
    myList.append(3)
    myList.append(4)
    myList.print_list()
    print("delete middle")
    myList.delete(2) # delete in middle
    myList.print_list()
    print("delte head")
    myList.delete(0) # delete at head
    myList.print_list()
    print("delete tail")
    myList.delete(1) # delete at tail
    myList.print_list()

    print("insert at head")
    myList.insert(0, 1)
    myList.print_list()
    print("insert at tail")
    myList.insert(2, 3)
    myList.print_list()
    print("insert in middle")
    myList.insert(2,2.5)
    myList.print_list()
    myList.print_backward()