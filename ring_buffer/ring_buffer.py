class RingBuffer:
    def __init__(self, capacity):
        self.index = 0
        self.capacity = capacity
        self.buffer = []

    def append(self, item):
        # check to see if buffer is not at capacity
        if len(self.buffer) == self.capacity:
            # self.buffer.pop()
            # self.buffer.append(item)
            self.buffer[self.index] = item
            self.index = (self.index + 1) % self.capacity
        else:
            self.buffer.append(item)

    def get(self):
        return self.buffer