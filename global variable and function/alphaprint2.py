#alphaprint2.py
sent=input("Enter a sentence:")
l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2=[]
for i in sent:
	l2.append(i)
print("original aplabets in input sentence")
print(l2)
print("-"*75)
s1=set(l1)
s2=set(l2)
s3=s1.difference(s2)
print("aplhabets not used in input sentence")
print("-"*75)
print(s3, len(s3))



	



