class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def reverse_linked_list(head):
    current = head
    temp = None
    
    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    
    if temp is not None:
        head = temp.prev
    return head

def print_list(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")


node1 = Node(3)
node2 = Node(10)
node3 = Node(2)
node4 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

node1.prev = None
node2.prev = node1
node3.prev = node2
node4.prev = node3

print("Original Linked List:")
print_list(node1)


reversed_head = reverse_linked_list(node1)

print("Reversed Linked List:")
print_list(reversed_head)
