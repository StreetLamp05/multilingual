from node import Node # import Node from node.py

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
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

    def delete(self, num):
        current = self.head

        if num == 0: # delete head
            self.head = self.head.next
            return
        elif num > (self.size - 1):
            raise Exception("Value out of range")
        elif num < (self.size - 1):
            i = 0;
            while i < num - 1: # go to node preceding the node to be deleted
                current = current.next
                i += 1
            current.next = current.next.next



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