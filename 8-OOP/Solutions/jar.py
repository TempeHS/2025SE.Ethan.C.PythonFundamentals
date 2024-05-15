class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return f"{self.size} of {self.capacity}"

    def deposit(self, n):
        return self.size + n

    def withdraw(self, n):
        return self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity == 12:
            self._capacity = capacity
        else:
            raise ValueError("Broken Capacity")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > 12:
            raise ValueError("Size Exceeds Capacity")
        if size < 0:
            raise ValueError("No Size")
        else:
            self._size = size
