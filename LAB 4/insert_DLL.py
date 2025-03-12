class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " )
            current = current.next
        print("None")

# Creating the doubly linked list
DLL = DLL()

DLL.insert_at_beginning(10)
DLL.insert_at_beginning(20)

DLL.insert_at_end(30)
DLL.insert_at_end(40)

# Printing the doubly linked list
print("\nDoubly linked list after inserting 30, 40 at the end: ")
DLL.print_list()
