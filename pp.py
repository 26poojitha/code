"""import numpy as np
a= list(map(int,input("enter 3 numbers for array a, space sepearted :").split()))
b= list(map(int,input("enter 3 numbers for array b, space sepearted :").split()))
a=np.array(a)
b=np.array(b)
v=np.vstack((a,b))
print("vertical stack :\n",np.vstack((a,b)))
print("horizantall stack: \n",np.hstack((a,b)))
print("Element 5 access",v[1,1])
print("Element 5 access",v[1][1])

import numpy as np
a= list(map(int,input("enter numbers for array:").split()))
a=np.array(a)
odd=a[a%2==1]
print(odd)

import numpy as np
a=list(map(int,input ("enter numbers for array").split()))
a=np.array(a)
a[a%2==1]=-1
print(a)"""

'''import numpy as np
a=list(map(int,input ("enter numbers for array").split()))
a=np.array(a,dtype=object)
a[a%2==1]=True
print(a)'''

'''import numpy as np
a=list(map(int,input ("enter numbers for array").split()))
a=np.array(a,dtype=object)
a[a%2==0]="Even"
print(a)'''

'''import numpy as np
a=list(map(int,input ("enter numbers for array").split()))
a=np.array(a,dtype=object)
b=a%3 == 0
print(b)'''

'''import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print("Element at [0,1]:",arr[0,1])
print("First row :",arr[0])
print("First column :",arr [:,0])
'''

'''import numpy as np
arr=np.array([1,2,3,np.nan,5])
print("ignoring NaN :",np.nanmean(arr))
print("Sum:",np.sum(arr)) 
print("std ignoring NaN:",np.std(arr[~np.isnan(arr)]))
'''

import numpy as np
arr=np.array([1.5,2.9,9.8])
print(arr.astype(np.int32))
arr=np.array([1,2,3,4])
print(arr.astype(np.float64))
arr=np.array([1.5,2.9,9.8])
print(arr.astype(str))
arr=np.array([0,1,7,0])
print(arr.astype(bool))
arr=np.array([True,True,False,True])
print(arr.astype(np.int32))
arr=np.array([1.5,2.9,9.8])
print(arr.astype(np.complex128))
arr=np.array([1,2,3,4])
print(arr.astype(np.int8))
arr=np.array([20250101,19990101])
print(arr.astype('datetime64[D]'))