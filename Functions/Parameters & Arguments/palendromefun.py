#palendromefun.py
def palendrome():
	n=int(input("enter a number:"))
	if(n<=0):
		print("{} is invalid input".format(n))
	else:
		tn=n
		r=0
		while(n>0):
			d=n%10
			r=r*10+d
			n=n//10
		else:
			if(tn==r):
				print("{} is palendrome".format(tn))
			else:
				print("{} is not palendrome".format(tn))
#main program
palendrome()

