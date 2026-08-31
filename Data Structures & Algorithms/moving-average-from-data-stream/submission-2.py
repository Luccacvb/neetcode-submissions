class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque([])

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
        else:
            self.window.popleft()
            self.window.append(val)

        total = sum(self.window) / float(len(self.window))
        return total


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
