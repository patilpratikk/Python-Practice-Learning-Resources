#posnegifelse.py
n=int(input("enter the number:"))
if(n==0):
    print("{} is zero".format(n))
else:
    if(n>0):
        print("{} is a positive  integer".format(n))
    else:
        print("{} is a negative integer".format(n))
print("\nprogram execution complete")