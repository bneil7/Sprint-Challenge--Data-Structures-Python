"""
RingBuffer has two methods, `append` and `get`. 

The `append` method adds the given element to the buffer. 
The `get` method returns all of the elements in the buffer in a list in their given order.

It should not return any `None` values in the list even if they are present in the ring buffer.
"""


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.index] = item
            self.index += 1  # increment by 1
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        if self.storage is not None:
            return self.storage
