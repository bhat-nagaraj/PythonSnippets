//Check whether two strings are anagrams or not

n1=input("enter string 1 ")
n2=input("enter string 2 ")

n1=sorted(n1)
n2=sorted(n2)

if n1==n2:
    print("true")
else:
    print("false")

    
