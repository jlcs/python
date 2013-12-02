class EmptyError:
    def __init__(self, msg):
        self._msg = msg

class Queue:
    INITIAL_LENGTH = 10
    
    def __init__(self):
        self._q = [None for i in range(Queue.INITIAL_LENGTH)]
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def resize(self):
        newq = [None for i in range(2*len(self._q))]
        for i in range(self._size):
            idx = (self._front + i) % len(self._q)
            newq[i] = self._q[idx]
        self._q = newq

    def __nonzero__(self):
        return self._size != 0

    def first(self):
        if self:
            return self._q[self._front]
        else:
            raise EmptyError("Attempting to access empty queue")

    def d(self):
        if self:
            value = self._q[self._front]
            self._q[self._front] = None
            self._front = (self._front + 1) % len(self._q)
            self._size -= 1
            return value
        else:
            raise EmptyError("Attempting to access empty queue")

    def q(self, o):
        if self._size == len(self._q):
            self.resize()
                            
        back = (self._front + self._size) % len(self._q)        
        self._q[back] = o
        self._size += 1
            
            


class Deq:
    INITIAL_LENGTH = 10

    def __init__(self):
        self._q = [None for i in range(Deq.INITIAL_LENGTH)]
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def resize(self):
        newq = [None for i in range(2*len(self._q))]
        for i in range(self._size):
            idx = (self._front + i) % len(self._q)
            newq[i] = self._q[idx]
        self._q = newq

    def __nonzero__(self):
        return self._size != 0

    def add_first(self, o):
        if self._size == len(self._q):
            self.resize()

        self._front = (self._front - 1) % len(self._q)
        self._q[self._front] = o
        self._size += 1

    def delete_first(self):
        if self:
            value = self._q[self._front]
            self._q[front] = None
            self._front = (self._front + 1) % len(self._q)
            self._size -= 1
            return value
        else:
            raise EmptyError("Attempting to access empty queue")

    def add_last(self, o):
        if self._size == len(self._q):
            self.resize()

        back = (self._front + self._size) % len(self._q)        
        self._q[back] = o
        self._size += 1

    def delete_last(self):
        if self:
            last = (self._front + self._size - 1) % len(self._q)
            value = self._q[last]
            self._q[last] = None
            self._size -= 1
            return value
        else:
            raise EmptyError("Attempting to access empty queue")

    def first(self):
        return self._q[self._front]

    def last(self):
        last = (self._front + self._size - 1) % len(self._q)
        return self._q[last]
