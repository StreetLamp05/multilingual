from node import Node # import Node from node.py

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def printSize(self):
        print(self.size)

    def append(self, value):
        new_node = Node(value)
        self.size += 1
        # if list empty
        if not self.head:
            self.head = new_node
            return
        # adding node to end of list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, value, num):
        new_node = Node(value)
        self.size += 1
        if num == 0: # add to beginning
            new_node.next = self.head
            self.head = new_node
        elif num == self.size - 1: # add to end
            current = self.head
            if not current:
                self.head = new_node
            while current.next:
                current = current.next
            current.next = new_node
        elif num > self.size or num <= 0:
            raise Exception('Invalid out of range')
        else: # add to middle
            current = self.head
            i = 0
            while i < (num - 1):
                current = current.next
                i += 1
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def delete(self, num):
        if self.size == 0:
            raise Exception('Empty linked list')
        elif num < 0 or num > (self.size - 1):
            raise Exception('Invalid index')
        elif num == 0: # delete head
            self.head = self.head.next
        elif num < self.size:
            current = self.head
            i = 0
            for i in range (0,num - 1):
                current = current.next
            current.next = current.next.next
            self.size -= 1

    def print_list(self):
        current = self.head
        print("Head -> Tail:")
        while current.next:
            print(current.value, "-> ", end="")
            current = current.next
        print(current.value)

if __name__ == "__main__":
    myList = LinkedList()
    myList.append(10)
    myList.append(20)
    myList.append(30)
    myList.append(40)
    myList.printSize()

    myList.print_list()
    print("Delete 30")
    myList.delete(2) # delete 30
    myList.print_list()
    print("Delete 40")
    myList.delete(2) # edge case (delete 40 at end of list)
    myList.print_list()
    print("Delete 10")
    myList.delete(0) # edge case (delete head)
    myList.print_list()

    myList.printSize()
    print("insert 25 (at tail)")
    myList.insert(25, 1)
    myList.print_list()
    print("insert 15 (at head)")
    myList.insert(15, 0)
    myList.print_list()
    print("insert 23 (in middle)")
    myList.insert(23, 2)
    myList.print_list()