#fibonaccifun.py
n=int(input("enter the number fibonacci numbers you want to get:"))
def fibofun(a):
	a=0
	b=1
	if(n==1):
		print(a)
	else:
		print(a)
		print(b)
		for i in range (2,n):
			c=a+b
			a=b
			b=c
			print(c)
#main program
fibofun(n)
