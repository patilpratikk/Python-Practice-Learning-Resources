#studentnamesorting
n=int(input("enter the number of students:"))
if(n<=0):
	print("{} is invalid input".format(n))
else:
	l=list()
	for i in range(1,n+1):
		sname=input("enter {} student name:".format(i))
		l.append(sname)
	else:
		print("original list l:{}".format(l))
		print("-"*70)
		l.sort()
		print("list in ascending order: {}".format(l))
		print("-"*70)
		l.sort(reverse=True)
		print("list in descending order: {}".format(l))
		print("*"*70)
