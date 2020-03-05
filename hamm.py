#http://rosalind.info/problems/hamm/
f = open('dataset', 'r').read().splitlines()

a = f[0]
b = f[1]
c = 0
d = 0

for i in a:
    if i != b[c]:
        d+=1
        
    c+=1
    
print(d)
