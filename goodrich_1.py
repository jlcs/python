# REINFORCEMENT
# _________________________________________________________________
def minmax(data):
    try:
        m = M = data[0]
        for val in data:
            if m > val:
                m = val
            elif M < val:
                M = val                
        return m,M
    except TypeError as e:
        print('hey')
        return -1

def sumsquares(n):
    try:
        return sum([k**2 for k in range(1,n+1)])
    except:
        print('no')

def sumoddsquares(n):
    try:
        return sum([k**2 for k in range(1,n+1) if k % 2 ==1])
    except TypeError as e:
        print(e)

def mychoice(l):
    try:
        i = random.randrange(0,len(l))
        return l[i]
    except:
        print('what!')
# _________________________________________________________________





# CREATIVITY
# _________________________________________________________________
def myreverse(l):
    return [l[i] for i in range(len(l)-1,-1,-1)]

def oddproduct(l):
    parity = [i & 1 for i in l]
    locations = [i for i in range(0,len(parity)) if parity[i] == 1]
    return False if len(locations) == 1 else locations

def reverseinput():
    l = []
    try:
        while 1:
            l.append(input())
    except EOFError:
        for i in range(1,len(l)+1):
            print(l[-i])

def dot(a,b):
    return sum([a[i]*b[i] for i in range(0,len(a))])

def overflow(l, i, val):
    try:
        l[i] = val
    except IndexError:
        print('no!')

def vowelCount(s):
    #s = list(s)
    vowels = ('a','e','i', 'o', 'u')
    vowelsInS = [i for i in s if (i in vowels)]
    return len(vowelsInS)

def pnorm(v, p):
    import math
    norm = 0
    for val in v:
        norm += val**p
    norm = norm**(1/p)
    return norm
# _________________________________________________________________





# PROJECTS
# _________________________________________________________________

def all_strings(letters):
    import pdb    
    letters = list(set(letters))
    pdb.set_trace()
    return all_strings_helper(letters, len(letters))

def all_strings_helper(letters, n):
    if (n ==1):
        return list(letters)
    else:
        l = []
        nMinusOneWords = all_strings_helper(letters, n-1)
        for letter in letters:
             l += [letter + word for word in nMinusOneWords if letter not in word]
        return l

def randomerrors():
    import string, random

    phrase = "I will never spam my friends again."
    
    numErrors = 8
    numLines = 20
    errorLines = []
    errorLocations = []
    errors = []
    
    for i in range(0,numErrors):
#        import pdb; pdb.set_trace()
        newErrorLine= random.randint(1,numLines)
        while newErrorLine in errorLines:
                    newErrorLine= random.randint(1,numLines)
        errorLines.append(newErrorLine)
        
        errorLocations.append(random.randint(0,len(phrase)))

        errorNumber = random.randint(0,len(string.printable)-1)        
        errors.append(string.printable[errorNumber])

    errorLines.sort()

    print(errorLines)
    print(errorLocations)
    print(errors)

    for i in range(1,numLines+1):
#        print(i)
        finalPhrase = list(phrase)
        if errorLines and i == errorLines[0]:
            finalPhrase[errorLocations.pop(0)] = errors.pop(0)
            errorLines.pop(0)
        print(''.join(finalPhrase))

def change(price, paid):
    if paid < price:
        raise ValueError('Not enough!')

    coins = {'quarters':25,  'dimes':10, 'nickels':5, 'cents':1}
    bills = {'thousands':1000, 'hundreds':100, 'fifties':50, 'twenties':20, 'tens':10, 'fives':5,  'ones':1 }
        
    change = paid - price
    dollars = int(change)
    cents = (change - int(change))*100

    billChange = dict()
    coinChange = dict()

    for coin in coins:
        current = cents % coins[coin]
        coinChange[coin] = current
        cents -= coins[coin]*(current)

    for bill in bills:
        current = dollars % bills[bill]
        billChange[bill] = current
        dollars -= bills[bill]*(current)

    return billChange, coinChange
