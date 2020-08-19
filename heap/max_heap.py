'''
Heap data structure

Heap Property - Max Heap
Shape Property - Fill values from left to right

Complexity:

Number of swaps - n
Number of checks - 2n
Convert list/array to heap O(n)
Heapify - O(lg n)
'''
class MaxHeap:
    def __init__(self, values = None):
        if values == None:
            self.ar = []
        else:
            self.ar = list(values)
        self.n = len(self.ar)
        
        start = self.n//2 - 1 
        for i in range(start, -1, -1):
            self.heapify(i)
    
    def extract_max(self):
        val = self.ar[0]
        self.n -= 1
        self.ar[0] = self.ar[self.n]
        self.heapify(0)
        return val
    
    def add(self, value):
        if self.n == len(self.ar):
            self.ar.append(value)
        else:
            self.ar[self.n] = value
        i = self.n
        self.n += 1
        
        while i > 0:
            parent = (i-1) // 2 
            if self.ar[parent] < self.ar[i]:
                self.ar[parent], self.ar[i] = self.ar[i], self.ar[parent]
                i = parent
            else:
                break
        
    def heapify(self, i):
        left = 2*i + 1
        right = 2*i + 2
        
        if left < self.n and self.ar[i] < self.ar[left]:
            largest = left
        else:
            largest = i 
        
        if right < self.n and self.ar[largest] < self.ar[right]:
            largest = right
        
        if largest != i:
            self.ar[i], self.ar[largest] = self.ar[largest], self.ar[i]
            self.heapify(largest)
    
    def print_heap(self):
        return self.ar
    
    def size(self):
        return self.n
