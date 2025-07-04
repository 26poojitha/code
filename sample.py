n=int(input("Enter the numerator:"))
d=int(input("Enter the denominator"))
try:
    quo=n/d
    print(quo)
except ZeroDivisionError:
    print("Denominator cant be zero")