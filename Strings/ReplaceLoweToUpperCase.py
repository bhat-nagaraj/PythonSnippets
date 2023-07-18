#replace all lowercase to uppercase

n1=input("enter string ")
res=''
for i in n1:
    if i.islower():
        i=i.upper()
        res=res+i
    else:
        res=res+i
print(res)