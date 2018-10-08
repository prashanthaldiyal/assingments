#question 1
print("Enter file name:")
fname=input()
p=open(fname,"r")
print(p.read(50))
p.close()

#question 2
import re
print("enter file name:")
fname=input()
k=0
w=input("enter a string:")
with open(fname,'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==w):
                k=k+1
print("Occurrences of the word:")
print(k)
p.close()

#question 3
print("enter file name:")
fname=input()
p=open(fname,"r")
fp=open("out.txt",'w')
for line in p:
   fp.write(line)
fp.close()
p.close()

#question 4
print("enter 1st file name:")
fname=input()
print("enter 2nd file name:")
sname=input()
p=open(fname,"r")
fp=open(sname,"a")
for line in p:
	fp.write(line)

fp.close()
p.close()	

#question 5
import random
r=[]
i=0
print("enter a file name:")
fname=input()
p=open(fname,"w")
for i in range(0,10):
	l=str(random.randint(1,10))
	p.write(l)
p.close()
p=open(fname,"r")
re=p.readline()
for line in re:
	line=line.split()
	if line:
		line=[int(i) for i in line]
		r.append(line)
p.close()    
p=open("out1.txt","w+")
r.sort()
for i in r:
	p.write('%s\n'%i)
p.close()	

