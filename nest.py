'''l2 = lambda a: lambda b,c:(a+b)*c
l1=l2(2)
value=l1(1,3)
print(value)'''

'''o=(lambda a: lambda b,c:(a+b)*c)(5)(3,2)
print(o)'''

'''num=int(input("a:"))
n =int(input("x: "))
oper = lambda a: lambda x:(x+a)**3
numsq=oper(num)
print(numsq(n))'''
'''
try:
    o=(lambda a: lambda b: lambda c,d:(a-b)/(c-d))(10)(4)(8,8)
    print(0)
except ZeroDivisionError:
    print("Division by zero error!!!")
except TypeError:
    print("Invalid Datatype!!!")
'''
'''o=(lambda a: lambda b: lambda c,d:a+'-'+b+'-'+c+'-'+d)('Hi')("Students")("Good","morning")
print(o)
'''
'''o=(lambda a: lambda b: lambda c,d:a.upper()[::-1]+' '+b+' '+c.upper()[::-1]+' '+d)("hi")("!")("students","!")
print(o)'''
'''

__del__():
const:
class abc():
    def __init__(self,v1,v2...):
        self.v1=v1
    def __del__(self):
        abc.v1
'''
'''
class opti():
    class_var=0
    print("Class variable",class_var)
    def __init__(self,var):
        opti.class_var+=10
        self.var=var
        print("Object variable:",var)
        print("Class variable",opti.class_var)
    def __del__(self):
        opti.class_var-=1
        print("obj var with %d is deleted" %self.var)
obj1=opti(10)
obj2=opti(12)
obj3=opti(13)
'''
'''
class calc:
    def __init__(self, a,b):
        self.a=a
        self.b=b
        print("Calc obj created......")
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def __del__(self):
        print("Created Calc obj was deleted")
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c= calc(a,b)
print("Addition:",c.add())
print("Subtraction:",c.sub())
del calc
'''
'''
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
my_circle = Circle(5)
area = my_circle.calculate_area()
print(f"The area of the circle is: {area:.2f}")
circumference = my_circle.calculate_circumference()
print(f"The circumference of the circle is: {circumference:.2f}")
'''
'''
class Numbers:
    def __init__(self,myList):
        self.myList=myList
    def __getitem__(self,index):
        return self.myList[index]
    def __setitem__(self,index,val):
        self.myList[index]=val
NumList=Numbers([1,2,3,4,5,6,7,8,9,10])
print(NumList[5])
NumList[3]=100
print(NumList.myList)

'''

