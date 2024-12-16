class Heap:
    def __init__(self):
        self.heap = [0] # first val is null, dummy

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1 # last index, to percolate up
        while i > 1 and self.heap[i] < self.heap[i // 2]: # curr is less than parent, swap
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 1 # iter back through arr

        
    def pop(self):
        # removing needs checks firs
        if len(self.heap) == 1:
            return None # no non null vals
        if len(self.heap) == 2:
            return self.heap.pop()
        
        min_val = self.heap[1]
        self.heap[1] = self.heap.pop() # replacement and removal same step
        i = 1 # we iterate from the root to percolate down

        while 2 * i < len(self.heap):
            left = 2 * i
            right = 2 * i + 1
            min_child = left

            # we check if right, because we need to ensure that child node exists first
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                min_child = right

            if self.heap[i] < self.heap[min_child]:
                break # its all in order for min heap

            # swap
            self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child

        return min_val