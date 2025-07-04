try:
    file=open('file1.txt')
    str=file.readline()
    strr=file.readline()
    print(str)
    print(strr)
except IOError:
    print("enter the correct file name")
else:
    print("successfully fetched the data")