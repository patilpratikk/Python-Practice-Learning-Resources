#reverse string
text=input("enter a word to be reversed:")
n=len(text)
for i in range(n-1,-1,-1):
	print(text[i])
print("-"*50)
for i in range(-1,-(n+1),-1):
    print(text[i])

