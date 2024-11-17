import ctypes
class DynamicArray:
    # constructor
    def __init__(self):
        self._ne = 0
        self._capacity = 1
        self._Arr = self._make_array(self._capacity) # ensure the extra space

    def __len__(self):
        return self._ne # return (n)um (e)lements
    
    def __getitem__(self, k): # where k is index specified
        if not 0 <= k < self._ne:
            raise IndexError("Index is out of bounds")
        return self._Arr[k]
    
    def append(self, obj): # public method
        # check if num elements is same size as capacity
        if self._ne == self._capacity:
            self._resize(2 * self._capacity) # double capacity
        # assign obj to curr last element index
        self._Arr[self._ne] = obj
        # increment last element index
        self._ne += 1

    def _resize(self, c):
        new_sized_arr = self._make_array(c)
        for k in range(self._ne):
            new_sized_arr[k] = self._Arr[k]
        self._Arr = new_sized_arr
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()
        
    
