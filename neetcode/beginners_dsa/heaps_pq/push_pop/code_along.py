class Heap:
    def __init__(self):
        self.heap = [0]

    def insert(self, val):
        # pushing appends to end, what if the order property messed up?
        # we must percolate up the heap, compare parent node (no need to check the other child of root node bc thats sorted + ensured)
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def delete(self):
        # check cases
        if len(self.heap) == 1:
            return None # since we do indexing from  1st index
        if len(self.heap) == 2:
            return self.heap.pop() # just return first index, which is 2
        
        mv = self.heap[1] # first node temp to return
        self.heap[1] = self.heap.pop() # reassign
        i = 1 # iter from here


        while 2 * i < len(self.heap): # ensure left child
            lc = 2 * i
            rc = 2 * i + 1
            mc = lc # assume

            # affirm min child val
            if rc < len(self.heap) and self.heap[rc] < self.heap[lc]:
                mc = rc

            # break stmt
            if self.heap[i] < self.heap[mc]:
                break # since curr idx val less than min val

            # recur swap
            self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

        return mv
