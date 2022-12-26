#primenumbers
n=int(input("enter a number:"))
if(n<=0):
	print("{} is invalid input".format(n))
else:
	for i in range(2,n+1):
		for m in range(2,n):
			if(i%m==0) and (i!=m):
				print("{} is not prime".format(i))
				break
		else:
			print("{} is prime".format(i))





		
		

