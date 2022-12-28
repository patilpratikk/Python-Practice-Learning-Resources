#missalpha.py
sent=input("Enter a sentence:")
l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2=l1
for i in sent:
	if(i in l1):
		l2.remove(i)
print(l2)


	


	



