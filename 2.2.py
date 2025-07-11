'''n=int(input())
c=0
for i in str(n):
    c+=1
print(c)

n=int(input())
c=0
for i in str(n):
    c+=int(i)
print(c)

n=int(input())
print(bin(n))'''

n=int(input())
m=bin(n)
print(m)
print(int(m,2))