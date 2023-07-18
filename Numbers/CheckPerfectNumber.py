n=int(input("enter number"))
sum=1
for i in range(2,n):
    if n%i==0:
        sum+=i
if n==sum:
    print("true")
else:
    print("false")
    
    

    
