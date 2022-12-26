#runnerupscore
a= map(int,input().split())
print(type(a))
print(sorted(list(set(a)))[-2])
print("---------------------OR-----------------------")
b=list(set(int(n) for n in input().split()))
b.sort()
print(b[-2])