#Find pairs of elements sum of which are equals to target element


list=[]
arr=[]
n=int(input("enter number of elements "))
#res=0
for i in range(0,n):
    ele=int(input("enter element"))
    arr.append(ele)
ele=int(input("enter target number "))

for i in range(0,n-1):
    for j in range(i+1,n):
        if arr[i]+arr[j]==ele:
            list.append((arr[i],arr[j]))
print(list)
