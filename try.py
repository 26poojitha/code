"""try:
    num=int(input("Enter the numbre:"))
    print(num*4)
except KeyboardInterrupt:
    print("number should be entered")
except ValueError:
    print("please try to give integer bot string")
print("okayy byeeeeee")"""
try:
    num=int(input("Enter the numbre:"))
    print(num*4)
except (KeyboardInterrupt,ValueError,TypeError):
    print("number should be entered")
print("okayy byeeeeee")