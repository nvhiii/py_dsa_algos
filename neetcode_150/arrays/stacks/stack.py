from dy_arr.dynamic_array import DynamicArray
class Stack(DynamicArray):
    def __init__(self, cap):
        super().__init__(cap)

    # 3 operations, push, pop, peek
    def push(self, obj):
        super().pushback(obj)

    def pop(self):
        if self._length > 0:
            super().popback()

    def peek(self):
        if self._length > 0:
            return self._Arr[self._length - 1]