class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def front_data(self):
        if self.front is None:
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        dequeued_data = temp.data
        del temp
        return dequeued_data

def serve_customers():
    customer_queue = Queue()

    # Enqueue 5 customers
    customer_ids = [101, 102, 103, 104, 105]
    for customer_id in customer_ids:
        customer_queue.enqueue(customer_id)

    # Serve customers
    print("Serving customers:")
    while not customer_queue.is_empty():
        customer_id = customer_queue.dequeue()
        print(f"Serving customer with ID: {customer_id}")

    # Check if the queue is empty
    if customer_queue.is_empty():
        print("All customers have been served. The queue is now empty.")

serve_customers()
