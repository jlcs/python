    return count
        count += 1 if s1[i]!=s2[i] else 0
    for i in range(len(s1)):
    count=0
        return None
    if len(s1) != len(s2):
def rosa6(s1, s2): #HAMM


    print("{0}\n{1}".format(maxkey, maxval))
    #return maxkey, maxval
            maxkey, maxval = key, GCcontent[key]        
        if GCcontent[key] > maxval:
    for key in string.keys():
    maxkey=''
    maxval=0
    GCcontent = {key:float(len(GCstrings[key])) / float(len(string[key])) for key in string.keys()}
    GCstrings = {key:''.join([c for c in string[key] if c in ['G', 'C']]) for key in string.keys()}
    string = {string[3*i]:string[3*i+1] + string[3*i+2] for i in range(len(string)//3)} # create hash with Rosalind_xxxx:GATGATCGC...
    string=string.split('\n')
def rosa_5(string): #GC
'''format of string: Rosalind_xxxx \n AGTCGTC.. \n AGTCTAG \n next line  '''

        
    return f[-1]
        f[i]=f[i-1]+k*f[i-2]
    for i in range(2,n):
    f[0]=f[1]=1
    f=[0]*n
def rosa_4(n,k): #FIB
    
    return ''.join([complements[c] for c in sequence])
    complements = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    sequence = sequence[::-1] #reverse
def rosa_3(sequence): #REVC

    return sequence.replace('T', 'U')
def rosa_2(sequence): #RNA

    return "{0} {1} {2} {3}".format(countA, countC, countG, countT)
    countT = sequence.count('T')
    countG = sequence.count('G')
    countC = sequence.count('C')
    countA = sequence.count('A')
def rosa_1(sequence): #DNA

import sys
