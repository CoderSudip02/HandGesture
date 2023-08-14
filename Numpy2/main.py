import numpy as np
arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,13]])
print(arr)
print(arr[1,1:4])
print(type(arr))
print(arr.shape)

print(np.__version__)
print(arr.ndim)
arr2=np.array([1,2,3,4],ndmin=1)
print(arr2)
print(arr2[:-3])
print(arr2.shape)

''''#Converting Data Type on Existing Arrays
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)'''