#Find two arrays are equal in length or not
arr1=[]
arr2=[]

n1=int(input("enter number of elements "))
for i in range(0,n1):
    ele=int(input("enter element"))
    arr1.append(ele)
    
n2=int(input("enter number of elements "))
for i in range(0,n2):
    ele=int(input("enter element"))
    arr2.append(ele)

if len(arr1)==len(arr2):
    print("true")
else:
    print("false")