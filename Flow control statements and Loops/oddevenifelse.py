#oddevenifelse
n=int(input("enter the number:"))
if (n%2)==0:
	print("{} is a even number".format(n))
else:
	if n==0:
		print("{} is even number".format(n))
	else:
		print("{} is odd number".format(n))
print("Program execution complete")
