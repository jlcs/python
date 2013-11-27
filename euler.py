# Problem 1
def sumWithoutMultiples(a,b,n):
    return sum([i for i in range(1,n) if i % a == 0 or i % b == 0])


# Problem 3
def sieve(n):
    sn = int(n/2) + 1
    l = range(1,n+1)
    for i in range(2,sn+1):
        l = [k for k in l if k == i or k % i != 0]
    return l

def largestPrimeFactor(n):
    sn = int(n/2) + 1
    l = sieve(sn)
    m = max([i for i in l if n % i == 0])
    return n if m == 1 else m


# Problem 14
class Queue:
    def __init__(self):
        self._l = []
        self._size = 0

    def q(self, o):
        self._l.insert(0,o)
        self._size += 1

    def d(self):
        try:        
            x = self._l.pop()
            self._size -= 1
            return x
        except IndexError:
            raise IndexError("Queue is empty")

    def __nonzero__(self):
        return bool(self._l)
    

def longestCollatz(n):
    ##    import os
    ##    os.chdir('C:\cygwin\home\user\python')
    ##    db = open("collatzdb.txt", "w") #DEBUG
    
    h = {}  # h[i] = length of Collatz sequence starting at i
    h[1] = 1
    
    q = []
    q.append(1)

    count = 1 # count is number of elements in the dict h that are <= n

    seqs = {}
    
    while count < n:                    
        a = q.pop(0)
        
        l = 2*a
        r = (a-1) / 3 if ((a-1) % 3 == 0 and a != 4 and ((a-1) / 3) % 2 == 1) else None
            
        h[l] = h[a] + 1
        # db.write("Added {0} to h, from {2}, with h[{0}] = {1}\r\n".format(l, h[l], a))#DEBUG        
        q.append(l)
        count += 1 if l <= n else 0        
        seqs[l] = a
        
        if r:
            h[r] = h[a]+1
            # db.write("Added {0} to h, from {2}, with h[{0}] = {1}\r\n".format(r, h[r], a)) #DEBUG            
            q.append(r)
            count += 1 if r <= n else 0
            seqs[r] = a
        
        q.sort()

    # db.close() # DEBUG
    return {key:h[key] for key in h.keys() if key in range(1,n+1)}, seqs


def collatz(n):
    seq = [n]
    
    if n == 1:        
        return seq
        
    while n != 1:
        if n % 2 == 0:
            n /= 2                        
        else:
            n = 3*n + 1        
        seq.append(n)

    return seq
