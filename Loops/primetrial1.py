#primenumdectforloop
n=int(input("enter a number:"))
if(n<=0):
        print("invalid input")
else:
        for i in range(2,(n//2)+1):
                if(n%i==0):
                        print("{} is not a prime number".format(n))
                        break
        else:
            print("{} is prime".format(n))
