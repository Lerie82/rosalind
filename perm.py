#http://rosalind.info/problems/perm/
from itertools import permutations
import re

f = open('dataset','r')
n = f.read()
p = []

for i in range(0,int(n)):
    i+=1
    p.append(i)

perm = permutations(p)
total = []

for i in list(perm):
    total.append(i)

a = len(total)
print(a)

for i in total:
    line = re.sub('[(),]','',str(i))
    print(line)
