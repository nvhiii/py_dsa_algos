from collections import deque

class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x) # o(1) operation, keep in mind queue is fifo meaning first item added is removed first, stack is lifo meaning last item added is removed first
    
    def pop(self):
        """
        :rtype: int
        """
        # since we are storing using a deque, we do fifo, but we need to reorganize the entire queue to make last item the first item since stack needs to remove last item, which in this case will need to be first
        for _ in range(len(self.q) - 1): # iterate until right before last element
            self.q.append(self.q.popleft()) # [1, 2, 3] -> since queue is popleft, we pop first 2 since iter until right before last element -> [2, 3, 1] -> [3, 2, 1]
        return self.q.popleft() # after reversing
        
    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.q[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()