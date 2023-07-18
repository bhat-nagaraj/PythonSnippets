#Find two arrays are equal in length or not
arr1=[]


n1=int(input("enter number of elements "))
for i in range(0,n1):
    ele=int(input("enter element"))
    arr1.append(ele)

arr1=sorted(arr1)
print("min is ",arr1[0])
print("max is ",arr1[n1-1])