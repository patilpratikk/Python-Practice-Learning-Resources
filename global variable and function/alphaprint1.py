#alphaprint1.py
sent=input("Enter a sentence:")
s1={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
m=len(s1)
for i in sent:
	s2=set()
	s2.add(i)
print(s2)
s3=s1.difference(s2)
print(s3)

