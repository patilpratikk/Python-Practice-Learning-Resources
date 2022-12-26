#basicsal
ename=input("Enter employee name: ")
eno=input("Enter empolyee number: ")
basicsal=float(input("enter your salary:"))
if(basicsal<=0):
	print("please enter valid salary")
else:
	if(basicsal>=10000):
		da=0.2*basicsal
		ta=0.15*basicsal
		hra=0.15*basicsal
		ma=0.05*basicsal
		gpf=0.02*basicsal
		lic=0.02*basicsal
	else:
		da=0.3*basicsal  
		ta=0.25*basicsal 
		hra=0.20*basicsal
		ma=0.10*basicsal 
		gpf=0.01*basicsal
		lic=0.01*basicsal
	netsal=(basicsal+da+ta+hra+ma)-(gpf+lic)
	print("*"*50)
	print("Employee name is {}".format(ename))
	print("Employee number is {}".format(eno))
	print("Employee Basic salary is {}".format(basicsal))
	print("Employee DA is {}".format(da))
	print("Employee TA is {}".format(ta))
	print("Employee HRA is {}".format(hra))
	print("Employee MA is {}".format(ma))
	print("Employee GPF deducted is {}".format(gpf))
	print("Employee LIC deducted is {}".format(lic))
	print("-"*50)
	print("Net salary of Employee is {}".format(netsal))
                
     
        
        

    
