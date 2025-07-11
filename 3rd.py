numbers=[]
num=int(input())
negative_c=0
non_negative=0
for n in range(1,num+1):
    n1=eval(input())
    numbers.append(n1)
for i in numbers:
    if i < 0:
        negative_c+=1
    else:
        non_negative+=1
print(negative_c)
print(non_negative)