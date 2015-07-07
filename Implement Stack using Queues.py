class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.deque1 = collections.deque()
        self.deque2 = collections.deque()
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.deque2:
            self.deque1.append(self.deque2.popleft())
        self.deque2.append(x)

    # @return nothing
    def pop(self):
        if not self.deque2:
            while len(self.deque1) > 1:
                self.deque2.append(self.deque1.popleft())
            self.deque1, self.deque2 = self.deque2, self.deque1
        return self.deque2.popleft()
        

    # @return an integer
    def top(self):
        if not self.deque2:
            val = self.pop()
            self.deque2.append(val)
        return self.deque2[0]

    # @return an boolean
    def empty(self):
        return not self.deque1 and not self.deque2
