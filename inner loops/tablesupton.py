#tablesupton
n=int(input("enter a number:"))
if(n<=0):
	print("{} is invalid input".format(n))
else:
	for i in range(1,n+1):
		print("-"*70)
		print("Table of {}".format(i))
		print("-"*70)
		for m in range(1,11):
			print("{} x {} = {}".format(i,m,i*m))