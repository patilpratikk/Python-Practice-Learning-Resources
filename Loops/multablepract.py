#multablepract.py
n=int(input("enter the number: "))
if(n<=0):
	print("invalid input. Please enter valid number")
else:
	i=1
	while(i<=10):
		print("{}*{}={}".format(n,i,n*i))
		i=i+1
