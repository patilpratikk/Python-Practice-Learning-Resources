#leapyear.py
n=int(input("enter the four digit year: "))
if(n>1000) and (n%400)==0:
    print(" {} is a leap year".format(n))
if(n>1000) and (n%4)==0 and (n%100)!=0:
    print(" {} is a leap year".format(n))
if(n>1000) and (n%4)!=0:
    print("the year {} is not a leap year".format(n))
if (n>1000) and (n%400)!=0 and (n%100)==0:
    print("the year {} is not a leap year".format(n))

