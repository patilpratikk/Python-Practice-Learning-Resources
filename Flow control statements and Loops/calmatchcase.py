#cal.py
d=["1-Addition",
   "2- Substraction", 
   "3- Multiplication",
   "4- Division",
   "5- Modulus Division",
   "6- Exponentation"]
print(d)
cho=int(input("enter the choice of operation to be performed:"))
match cho:
	case 1:
		a=float(input(" enter the first value:"))
		b=float(input(" enter the second value:"))
		print(" the sum of {} and {} is {}".format(a,b,a+b))
	case 2:
		a=float(input(" enter the first value:"))
		b=float(input(" enter the second value:"))
		print(" the substraction of {} and {} is {}".format(a,b,a-b))
	case 3:
		a=float(input(" enter the first value:"))
		b=float(input(" enter the second value:"))
		print(" the multiplication of {} and {} is {}".format(a,b,a*b))
	case 4:
		a=float(input(" enter the first value:"))
		b=float(input(" enter the second value:"))
		print(" the division of {} and {} is {}".format(a,b,a/b))
	case 5:
		a=float(input(" enter the first value:"))
		b=float(input(" enter the second value:"))
		print(" the mod div of {} and {} is {}".format(a,b,a%b))
	case 6:
		a=float(input(" enter the first value:"))
		b=float(input(" enter the second value:"))
		print("  {} to the power {} is {}".format(b,a,a**b))
print(" program execution is over")

