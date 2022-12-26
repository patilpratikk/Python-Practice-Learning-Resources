#marksreportpract
while(True):
	stno=int(input("enter student roll number:"))
	if(stno>0) and(stno<=100):
		break
sname=input("enter student name:")
while(True):
	cm=int(input("enter the marks obtained in C:"))
	if(cm>=0) and (cm<=100):
		break
while(True):
	cppm=int(input("enter the marks obtained in CPP:"))
	if(cppm>=0) and (cppm<=100):
		break
while(True):
	pym=int(input("enter the marks obtained in Python:"))
	if(pym>=0) and (pym<=100):
		break
totmarks=cm+cppm+pym
permarks=(totmarks/300)*100
if (cm<40) or (cppm<40) or (pym<40):
	grade=" the candidate is fail"
else:
	if(totmarks>=250) and (totmarks<=300):
		grade="Passed with DISTINCTION"
	elif(totmarks>=200) and (totmarks<=249):
		grade="Passed in First Class"
	elif(totmarks>=150) and (totmarks<=199):
		grade="Passed in Second Class"
	elif(totmarks>=120) and (totmarks<=149):
		grade="Passed in Third Class"
	elif(cm<40) or (cppm<40) or (pym<40):
		grade="Failed"
print("*"*50)
print("\tStudent Report Card")
print("*"*50)
print("\tCandidate Roll number:{}".format(stno))
print("\tCandidate Name:{}".format(sname))
print("\tCandiate Marks in C:{}".format(cm))
print("\tCandidate Marks in CPP:{}".format(cppm))
print("\tCandidate Marks in Python:{}".format(pym))
print("-"*50)
print("\tTotal marks obtained by {}:{}".format(sname,totmarks))
print("\tGrade awarded to {}: {}".format(sname,grade))