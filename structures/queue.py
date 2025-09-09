class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def front(self):
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items


if __name__ == "__main__":
    queue = Queue()
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print("Queue:", queue.display())
    print("Size:", queue.size())
    print("Front:", queue.front())
    
    dequeued = queue.dequeue()
    print("Dequeued:", dequeued)
    print("Queue after dequeue:", queue.display())
    
    print("Is empty:", queue.is_empty())
