class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.items.pop(0)
            print(f"Dequeued: {removed_item}")
            return removed_item
        else:
            print("Queue is empty, cannot dequeue")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.dequeue()  # Output: Dequeued: 1
queue.dequeue()  # Output: Dequeued: 2
queue.dequeue()  # Output: Dequeued: 3
queue.dequeue()  # Output: Queue is empty, cannot dequeue
