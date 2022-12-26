# Write a Python program for calculating Compound intrest and total sum to pay
# CI= p(1+(r/100))**n-p
#compoundintrest
p=float(input("\tenter the principal amount:"))
n=float(input("\tenter the number of years:"))
r=float(input("\tenter the rate of intrest:"))
CI=p*((1+(r/100))**n)-p
Total_amount=p*(1+(r/100))**n
print("-"*100)
print("\tthe value of principal:{} ".format(p))
print("\tnumber of years for which amount is invested is:{} ".format(n))
print("\tthe rate of intrest is: {}".format(r))
print("\tcompound intrest calculated on the principal of {} at {} rate for {} years is: {}".format(p,r,n,CI))
print("\ttotal amount to be paid= ", Total_amount)
print("-"*100)
