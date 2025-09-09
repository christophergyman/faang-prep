class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_val
    
    def heapify_down(self, i):
        while True:
            smallest = i
            left = self.left_child(i)
            right = self.right_child(i)
            
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest == i:
                break
            
            self.swap(i, smallest)
            i = smallest
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)
    
    def display(self):
        return self.heap


class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max_val
    
    def heapify_down(self, i):
        while True:
            largest = i
            left = self.left_child(i)
            right = self.right_child(i)
            
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            
            if largest == i:
                break
            
            self.swap(i, largest)
            i = largest
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)
    
    def display(self):
        return self.heap


if __name__ == "__main__":
    print("MinHeap Example:")
    min_heap = MinHeap()
    
    min_heap.insert(3)
    min_heap.insert(1)
    min_heap.insert(4)
    min_heap.insert(1)
    min_heap.insert(5)
    
    print("MinHeap:", min_heap.display())
    print("Peek:", min_heap.peek())
    print("Extract min:", min_heap.extract_min())
    print("MinHeap after extract:", min_heap.display())
    
    print("\nMaxHeap Example:")
    max_heap = MaxHeap()
    
    max_heap.insert(3)
    max_heap.insert(1)
    max_heap.insert(4)
    max_heap.insert(1)
    max_heap.insert(5)
    
    print("MaxHeap:", max_heap.display())
    print("Peek:", max_heap.peek())
    print("Extract max:", max_heap.extract_max())
    print("MaxHeap after extract:", max_heap.display())
