class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items


if __name__ == "__main__":
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print("Stack:", stack.display())
    print("Size:", stack.size())
    print("Peek:", stack.peek())
    
    popped = stack.pop()
    print("Popped:", popped)
    print("Stack after pop:", stack.display())
    
    print("Is empty:", stack.is_empty())
