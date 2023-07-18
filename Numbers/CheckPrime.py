

n=int(input("enter"))
if n==1:
    print("false")
if n==2:
    print("true")
else:
    for i in range(2,n):
        if n%i==0:
            print("false")
            exit()
    print("true")
    
