class MovingAverage:
    def __init__(self, size: int):
        self.max_size = size
        self.cur_size = 1
        self.values = [0] * size
        self.index = 0
        self.window_sum = 0
        self.prev = 0

    def next(self, val: int) -> float:
        self.prev = self.values[self.index]
        self.window_sum -= self.prev
        self.window_sum += val
        self.values[self.index] = val
        self.index = (self.index + 1) % self.max_size

        calculate = self.window_sum / self.cur_size

        if self.cur_size < self.max_size:
            self.cur_size += 1

        return calculate


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
