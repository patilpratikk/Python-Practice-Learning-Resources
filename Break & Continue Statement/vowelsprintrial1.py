#vowelsprint
text=input("enter line of text:")
l1=['a','e','i','o','u','A','E','I','O','U']
n=(len(text))
for i in range(0,n):
	for vow in l1:
		if(text[i]==vow):
			print(vow)
print("*"*80)


