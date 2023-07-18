n=int(input("enter"))
count=len(str(n))
temp=n
sum=0

while temp>0:
    digit=temp%10
    sum+=digit**count
    temp=temp//10
    
if sum==n:
    print("armstrong")
else:
    print("not armstrong")
    
