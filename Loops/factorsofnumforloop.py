#factorsofnumforloop
n=int(input("enter a number:"))
if(n<0):
    print("invalid input")
else:
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
                
