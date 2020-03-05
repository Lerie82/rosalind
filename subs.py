#http://rosalind.info/problems/subs/
#must figure the length of the f[1] instead of manually placing ints (line 14)

def split(word): 
    return [char for char in word] 
    
f = open('dataset', 'r').read().splitlines()
a = split(f[0])
i = 0
b = f[1]

for s in a:
    try:
        w = a[i] + a[i+1] + a[i+2] + a[i+3]+ a[i+4] + a[i+5] + a[i+6]+ a[i+7] + a[i+8]
    except:
        break
    
    if w == b:
        print(i+1, end = ' ')
        
    i+=1

print()
