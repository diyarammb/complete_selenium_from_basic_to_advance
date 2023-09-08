import numpy as np
# class Binary_Seacrch():
def binarySearch(arr,l,r,x):
    if r>=1:
       mid =1+(r-1)//2
       if arr[mid]==x:
         return mid
       elif arr[mid]>x:
           return binarySearch(arr, l, mid - 1, x)
       else:
            return  binarySearch(arr,mid+1,r,x)
arr=np.array([2,3,4,10,40])
x=10
result=binarySearch(arr,0,len(arr)-1,x)
if result!=1:
    print("Element present at index %d"%result)
else:
    print("Element is not present in Array")

