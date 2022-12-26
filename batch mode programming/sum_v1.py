# practice sets 1
# sum operation using input() function
print("enter the value of first number") #displays the message
x=input() #stores or reads the input from keyboard and puts it into variable x
print(" enter the value of second number")
y=input()
# now as we know that input function stores every information in str, we need to convert str datatype to float or int data type so that mathematical operation can be performed
a=int(x)
b=int(y)
c=a+b
print("-"*50)
print(" The sum of {} and {} is {}".format(a,b,c))
