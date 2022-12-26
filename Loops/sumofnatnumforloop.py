#sumofnatnumforloop.py
n=int(input("enter the number:"))
if(n<=0):
	print("invalid input")
else:
	s=0
	ssq=0
	cs=0
	for i in range(1,n+1):
		s=s+i
		ssq=ssq+i**2
		cs=cs+i**3
	print("the sum of first {} natural numbers is {}".format(n,s))
	print("the sum of squares of first {} natural numbers is {}".format(n,ssq))
	print("the sum of cubes of first {} natural numbers is {}".format(n,cs))