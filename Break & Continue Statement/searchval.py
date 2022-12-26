#searchval.py
n=int(input("enter the number of values to be added in the list:"))
if(n<=0):
	print("{} is invalid input".format(n))
else:
	l1=list()
	for i in range(1,n+1):
		val=input("enter {} value to be added:".format(i))
		l1.append(val)
m=input("enter value to be searched:")
for v in l1:
	if(m==v):
		print("value matched in list")
		break
else:
	print("value did not found in list")

