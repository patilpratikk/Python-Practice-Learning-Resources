#numacsdes.py
n=int(input("enter how many values u want to arrange:"))
if(n<=0):
	print("{} is invalid input".format(n))
else:
	l=list()
	for i in range(1,n+1):
		val=float(input("enter {} value:".format(i)))
		l.append(val)
	else:
		print("original contents (random) of l")
		print("*"*100)
		print("contents of l={}".format(l))
		l.sort()
		print("contents of l in ascending order:{}".format(l))
		print("-"*100)
		(l.sort(reverse=True))
		print("contents of l in descending order:{}".format(l))


