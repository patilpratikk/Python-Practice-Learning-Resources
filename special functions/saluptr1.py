#saluptr1.py
emps1=lambda a: a>10,000
emps2=lambda b: b<=10,000
print("Enter employee salaries seperated by space")
lst=[int(sal) for sal in input().split()]
empclass1=list(filter(emps1,lst))
empclass2=list(filter(emps2,lst))
