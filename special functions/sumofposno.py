#sumofposno.py
import functools
pos=lambda a:a>0
print("Enter List of elements separated bny space:")
lst=[int(val) for val in input().split()]
posno=list(filter(pos,lst))
sumop=functools.reduce(lambda b,c:b+c, posno)
print("Sum of pos no.= ",sumop)