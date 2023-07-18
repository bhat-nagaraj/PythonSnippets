def func(n):
    if n<0:
        print("incorrect")
    if n==1 or n==2:
        return 1
    else:
        return func(n-1)+func(n-2)
        
print(func(9))