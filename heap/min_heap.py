'''
Heap data structure

Heap Property - Min Heap
Shape Property - Fill values from left to right

Complexity:

Number of swaps - n
Number of checks - 2n
Convert list/array to heap O(n)
Heapify - O(lg n)
'''


class MinHeap:
    def __init__(self, values=None):
        if values is None:
            self.ar = []
        else:
            self.ar = list(values)
        self.n = len(self.ar)

        start = self.n // 2 - 1
        for i in range(start, -1, -1):
            self.heapify(i)

    def pop(self):
        if self.n == 0:
            raise ValueError
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
            if self.ar[parent] > self.ar[i]:
                self.ar[parent], self.ar[i] = self.ar[i], self.ar[parent]
                i = parent
            else:
                break

    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.n and self.ar[left] < self.ar[i]:
            smallest = left
        else:
            smallest = i

        if right < self.n and self.ar[right] < self.ar[smallest]:
            smallest = right

        if smallest != i:
            self.ar[smallest], self.ar[i] = self.ar[i], self.ar[smallest]
            self.heapify(smallest)


