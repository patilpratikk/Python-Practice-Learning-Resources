#salupdation.py
import functools 
emps1=lambda a: a>10000
emps2=lambda b: b<=10000
print("Enter employee salaries seperated by space")
lst=[int(sal) for sal in input().split()]
empclass1=list(filter(emps1,lst))
empclass2=list(filter(emps2,lst))
empcls1up=list(map(lambda sal:1.15*sal,empclass1))
empcls2up=list(map(lambda sal:1.2*sal,empclass2))
totoldsalpaidcl1=functools.reduce(lambda p,q:p+q,empclass1)
totoldsalpaidcl2=functools.reduce(lambda p,q:p+q,empclass2)
totnewsalpaidcls1=functools.reduce(lambda p,q:p+q,empcls1up)
totnewpaidcls2=functools.reduce(lambda p,q:p+q,empcls2up)
total_ctc_old=totoldsalpaidcl1+totoldsalpaidcl2
total_ctc_new=totnewsalpaidcls1+totnewpaidcls2
print("All Employees sal in the company:", lst)
print("-"*100)
print("Employees with less than 10,000 sal:", empclass2)
print("Updated sal of Employees with less than 10,000 sal:", empcls2up)
print("-"*100)
print("Employees with more than 10,000 sal:", empclass1)
print("Updated sal of Employees with more than 10,000 sal:", empcls1up)
print("="*100)
print("Total cost to company by Class 1 employees earlier:", totoldsalpaidcl1)
print("Total cost to company by Class 2 employees earlier:", totoldsalpaidcl2)
print("-"*100)
print("Total cost to company by Class 1 employees now:", totnewsalpaidcls1)
print("Total cost to company by Class 2 employees now:", totnewpaidcls2)
print("="*100)
print("Total cost to company by all employees earlier:", total_ctc_old)
print("Total cost to company by all employees now:", total_ctc_new)
