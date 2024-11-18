class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int):
        self.stack.append(val)
        if not self.min_stack or self.getMin() < val: # not ensures we dont do a check in min without first appending
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            if self.top() == self.getMin():
                self.min_stack.pop()
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]