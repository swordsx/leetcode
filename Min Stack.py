class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if self.stack:
            self.stack.append((x, min(x, self.getMin())))
        else: self.stack.append((x, x))
        return x

    # @return nothing
    def pop(self):
        self.stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1][0]

    # @return an integer
    def getMin(self):
        return self.stack[-1][1]
