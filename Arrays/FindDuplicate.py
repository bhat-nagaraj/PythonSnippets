#Find duplicates in the array


arr=[]
n=int(input("enter number of elements "))
#res=0
for i in range(0,n):
    ele=int(input("enter element"))
    arr.append(ele)
for i in range(0,n-1):
    for j in range(i+1,n):
        if arr[i]==arr[j] and arr[j]!=0:
            print(arr[i])
            arr[j]=0