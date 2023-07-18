#Merge two Arrays

arr=[]
res=[]

n1=int(input("enter number of elements "))
for i in range(0,n1):
    ele=int(input("enter element"))
    arr.append(ele)
    
n2=int(input("enter number of elements "))
for i in range(0,n2):
    ele=int(input("enter element"))
    res.append(ele)
    

for i in range(0,n2):
    arr.append(res[i])
print(arr)
    
