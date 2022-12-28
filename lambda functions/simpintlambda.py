#Simpleintlambda
simpint=lambda p,r,n:(p*n*r)/100
p=float(input("enter principal amount:"))
r=float(input("enter rate of intrest:"))
n=float(input("enter time period:"))
simint=simpint(p,n,r)
print("simpleint on principal of {} at rate of {} for time period of {} yeras is {}".format(p,r,n,simint))
print("------------------or-------------------")
print("simpleint ={} ".format(simpint(float(input("enter principal amount:")),float(input("enter rate of intrest:")),float(input("enter time period:")))))