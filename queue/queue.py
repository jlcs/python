class Queue:
    def __init__(self):
        self._l = []
        self._size = 0    

    def push(self, o):
        self._l.insert(0,o)
        self._size += 1

    def pop(self):
        try:        
            x = self._l.pop()
            self._size -= 1
            return x
        except IndexError:
            raise IndexError("Queue is empty")
