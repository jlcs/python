class EmptyError:
    def __init__(self, msg):
        pass

class Stack:
    def __init__(self, initial=None):        
        if initial and isinstance(initial, list):
            self._l = [o for o in initial]            
            return
        self._l = []

    def push(self, o):
        self._l.append(o)

    def pop(self):
        if not self:
            raise EmptyError("Attempting to pop empty stack")
        return self._l.pop()

    def top(self):
        if not self:
            raise EmptyError("Attempting to top empty stack")
        return self._l[-1]

    def __nonzero__(self):
        return len(self._l) != 0

    def __len__(self):
        return len(self._l)

def reverse_file(infile, outfile):
    f = open(infile, 'r')
    s = Stack()

    for line in f.readlines():
        s.push(line.rstrip('\n\r'))
    f.close()

    f = open(outfile, 'w')
    while s:
        f.write(s.pop() + '\r\n')
    f.close()
    
def is_matched(expr):
    lefts = {'{', '(', '['}
    rights = {'{':'}', '(':')', '[':']'}
    s = Stack()
    for c in expr:
        if c in lefts:
            s.push(c)
        elif c in rights.values():
            if not s:
                return False
            elif c != rights[s.top()]:
                return False
            else:
                s.pop()
    return not s
