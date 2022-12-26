#squareop4
def squareoprt():
	n=float(input("enter a number"))
	b=n*n
	return n,b
#main program
n,b=squareoprt()
print("the square of {} is {}".format(n,b))
print("-------------------------or------------------------------")
sq= squareoprt()
print("the square of {} is {}".format(sq[0],sq[1])) 