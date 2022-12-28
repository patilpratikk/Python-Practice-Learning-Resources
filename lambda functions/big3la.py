#big3
big=lambda a,b,c: "Equal" if ((a==b ) and (b==c) and (a==c)) else a if ((a>b) and (a>c)) else b if ((b>c) and (b>a)) else c 
print("big={} ".format(big(float(input("enter a:")),float(input("enter b:")),float(input("enter c:")))))
print("-----------------or-------------------")
big3=lambda a,b,c: "Equal" if ((a==b ) and (b==c) and (a==c)) else a if (a>b) else b if (b>c) else c   
print("big={} ".format(big(float(input("enter a:")),float(input("enter b:")),float(input("enter c:")))))



