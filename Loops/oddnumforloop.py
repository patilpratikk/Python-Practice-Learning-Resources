#oddnumforloop.py
n=int(input("enter the number:"))
if(n<=0):
	print("invalid number")
else:
	for i in range(n,0,-1):
		if(i%2!=0):
			print(i)

		
