# Write a Python program for calculating simple intrest and total sum to pay
# SI= npr/100
#simpleintrest
p=float(input("\tenter the principal amount:"))
n=float(input("\tenter the number of years:"))
r=float(input("\tenter the rate of intrest:"))
SI=(n*p*r)/100
Total_amount=(p+SI)
print("-"*100)
print("\tthe value of principal:{} ".format(p))
print("\tnumber of years for which amount is invested is:{} ".format(n))
print("\tthe rate of intrest is: {}".format(r))
print("\tsimple intrest calculated on the principal of {} at {} rate for {} years is: {}".format(p,r,n,SI))
print("\ttotal amount to be paid= ", Total_amount)
print("-"*100)
