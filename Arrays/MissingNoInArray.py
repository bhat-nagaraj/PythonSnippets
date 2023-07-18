#Find missing number in the array


arr=[]
n1=int(input("enter number of elements "))
res=0
for i in range(0,n1-1):
    ele=int(input("enter element"))
    arr.append(ele)
sum=(n1*(n1+1))/2
for i in range(n1-1):
    res=res+arr[i]
print(int(sum-res))    