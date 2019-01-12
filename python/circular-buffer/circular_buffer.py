from collections import deque

class BufferFullException(Exception):
    def __init__(self):
        super().__init__('Buffer is Full, try to clear or overwrite')


class BufferEmptyException(Exception):
    def __init__(self):
        super().__init__('You cannot read an empty buffer')


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque()

    def read(self):
        try:
            return self.buffer.popleft()
        except:
            raise BufferEmptyException()

    def write(self, data):
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            raise BufferFullException


    def overwrite(self, data):
        try:
            self.write(data)
        except:
            _ = self.read()
            self.write(data)

    def clear(self):
        self.buffer.clear()
