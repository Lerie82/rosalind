#http://rosalind.info/problems/ini/

f = open('dataset','r').read()

a = str(f.count('A'))
c = str(f.count('C'))
g = str(f.count('G'))
t = str(f.count('T'))

print(a+' '+c+' '+g+' '+t)
