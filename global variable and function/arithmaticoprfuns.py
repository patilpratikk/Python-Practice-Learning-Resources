#arithmaticoprfuns
while(True):
	def addno():
		a=float(input("Enter first number"))
		b=float(input("Enter second number"))
		c=a+b
		print("The sum of {} and {} is {}".format(a,b,c))
	def subno():
		a=float(input("Enter first number"))
		b=float(input("Enter Second number"))
		c=a-b
		print("{}-{}={}".format(a,b,c))
	def mult():
		a=float(input("Enter first number:"))
		b=float(input("Enter second number:"))
		c=a*b
		print("The product of {} and {} is {}".format(a,b,c))
	def divi():
		a=float(input("Enter first number:"))
		b=float(input("Enter second number:"))
		c=a/b
		print("{} divided by {} is {}".format(a,b,c))
	def modulodivi():
		a=float(input("Enter first number:"))
		b=float(input("Enter second number:"))
		c=a%b
		print("When {} is divided by {}, we get remainder {}".format(a,b,c))
	#main program
	print("--------------------------------------------------------------")
	print("\tArithmatic Oprators Menu")
	print("--------------------------------------------------------------")
	print("\t1.Addition","\n\t2.Substration","\n\t3.Multiplication", "\n\t4.Division","\n\t5.ModuloDivision","\n\t6.Exit")
	ch=int(input("Enter Your Choice of Operation:"))
	match ch:
		case 1:
			addno()
		case 2:
			subno()
		case 3:
			mult()
		case 4:
			divi()
		case 5:
			modulodivi()
		case 6:
			exit()
		case _:
			print("Invalid Choice. Please enter proper option choice")



