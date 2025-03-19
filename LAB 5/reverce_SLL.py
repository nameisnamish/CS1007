class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None  # prev is a new tail
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
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

print("Original Linked List:")
print_list(node1)

reversed_head = reverse_linked_list(node1)

print("Reversed Linked List:")
print_list(reversed_head)
