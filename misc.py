class MagicSquareIterator:
    def __init__(self, current = 3, maximum=20):
        self.current = current-1
        self.max = maximum

    def __iter__(self):
        return self

    def formula(self):
        return self.current * (self.current**2 + 1)//2

    def __next__(self):
        self.current += 1
        if self.current > self.max:
            raise StopIteration    
        return self.formula()

if __name__ == '__main__':
    a = MagicSquareIterator(5)
    for val in a:
        print(val)


def CharacterRuns(n):
    n_str = [i for i in str(n)]
    l = [] # list of runs
    i = 0
    while (i < len(n_str)):
        currChar = n_str[i]
        l_temp = [currChar]
        while (i < len(n_str)-1 and n_str[i] == n_str[i+1]):
            l_temp.append(currChar)
            i+=1
        i+=1
        l.append(l_temp)
    return l, [len(run) for run in l]

#class LookAndSay(Progression):
#    def __init__(self, start=1):
