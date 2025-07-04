'''try:
    num=11
    print(num)
    raise ValueError
except:
    print("exception occured")


try:
    print("Raising exception")
    raise ValueError
finally:
    print("Performing error")


c=int(input("Enter temperature in c:"))
f=(c*9/5)+32
assert(f<=32),"its cold"
print("Farenheit:",f)'''

def display(n):
    while True:
        try:
            n+=1
            if n==21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n,end=" ")
i=0
display(i)