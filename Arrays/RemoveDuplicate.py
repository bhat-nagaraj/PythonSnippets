#Remove duplicate from array type-1
arr=[]
n=int(input("enter number of elements "))

for i in range(0,n):
    ele=int(input("enter element"))
    arr.append(ele)

res=[*set(arr)]
print(res)

#Remove duplicate from array type-2
arr1=[]
n1=int(input("enter number of elements "))
res1=[]
for i1 in range(0,n1):
    ele1=int(input("enter element"))
    arr1.append(ele1)
    
for i1 in range(0,n1):
    if arr1[i1] not in res1:
        res1.append(arr1[i1])
print(res1)

        
    