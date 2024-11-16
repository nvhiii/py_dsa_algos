from empty import Empty

class ArrayQueue(Empty):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[0]
    
    def enqueue(self, e):
        self._data.append(e) # adds to end of list starting at first idx

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data.pop(0) # get rid of first index
    
