#Left rotate the array

arr=[]
res=[]
count=0
n=int(input("enter number of elements "))
for i in range(0,n):
    ele=int(input("enter element"))
    arr.append(ele)
    
for i in range(2,n):
    res.append(arr[i])
for i in range(0,2):
    res.append(arr[i])
   
print(res)