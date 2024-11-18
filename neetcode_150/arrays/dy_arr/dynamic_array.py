class DynamicArray:
    def __init__(self, capacity=1): # default cap of 1
        self._length = 0
        self._capacity = capacity
        self._Arr = [0] * capacity

    def resize(self):
        # double capacity
        self._capacity = 2 * self._capacity
        # create new arr
        new_arr = [0] * self._capacity
        # move items from curr to new arr
        for i in range(self._length):
            new_arr[i] = self._Arr[i]
        # garbage collection, get rid of reference to old arr
        self._Arr = new_arr
    
    def get(self, i):
        return self._Arr[i]
    
    def set(self, i, n):
        self._Arr[i] = n # accessing is o(1)

    def pushback(self, obj): # push obj to end
        if self._length == self._capacity:
            self.resize()
        self._Arr[self._length] = obj
        self._length += 1

    def popback(self):
        if self._length > 0:
            self._length -= 1
            return self._Arr[self._length]
        else:
            return None

    def getSize(self):
        return self._length
    
    def getCapacity(self):
        return self._capacity