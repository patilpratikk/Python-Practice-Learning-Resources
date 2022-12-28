#sumofposandegno.py
import functools
pos=lambda a:a>0
neg=lambda b:b<0
lst=[int(x) for x in input().split()]
posno=list(filter(pos,lst))
negno=list(filter(neg,lst))
sumpos=functools.reduce(lambda p,q:p+q,posno)
sumneg=functools.reduce(lambda p,q:p+q,negno)
print("Sum of positive numbers is ",sumpos)
print("Sum of negative numbers is ",sumneg)