#Reverse the given array
arr=[]
n=int(input("enter number of elements "))

for i in range(0,n):
    ele=int(input("enter element"))
    arr.append(ele)

res=[]
i=n-1
while i>=0:
    res.append(arr[i])
    i=i-1
print(res)

        
    