import sys

def rosa_1(sequence): #DNA
    countA = sequence.count('A')
    countC = sequence.count('C')
    countG = sequence.count('G')
    countT = sequence.count('T')
    return "{0} {1} {2} {3}".format(countA, countC, countG, countT)

def rosa_2(sequence): #RNA
    return sequence.replace('T', 'U')

def rosa_3(sequence): #REVC
    sequence = sequence[::-1] #reverse
    complements = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join([complements[c] for c in sequence])
    
def rosa_4(n,k): #FIB
    f=[0]*n
    f[0]=f[1]=1
    for i in range(2,n):
        f[i]=f[i-1]+k*f[i-2]
    return f[-1]
        

'''format of string: Rosalind_xxxx \n AGTCGTC.. \n AGTCTAG \n next line  '''
def rosa_5(string): #GC
    string=string.split('\n')
    string = {string[3*i]:string[3*i+1] + string[3*i+2] for i in range(len(string)//3)} # create hash with Rosalind_xxxx:GATGATCGC...
    GCstrings = {key:''.join([c for c in string[key] if c in ['G', 'C']]) for key in string.keys()}
    GCcontent = {key:float(len(GCstrings[key])) / float(len(string[key])) for key in string.keys()}
    maxval=0
    maxkey=''
    for key in string.keys():
        if GCcontent[key] > maxval:
            maxkey, maxval = key, GCcontent[key]        
    #return maxkey, maxval
    print("{0}\n{1}".format(maxkey, maxval))


def rosa6(s1, s2): #HAMM
    if len(s1) != len(s2):
        return None
    count=0
    for i in range(len(s1)):
        count += 1 if s1[i]!=s2[i] else 0
    return count
