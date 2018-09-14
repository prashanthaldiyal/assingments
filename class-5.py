#question 1
print("enter any year:")
year=int(input())
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("it is a leap year")
       else:
           print("it is not a leap year")
   else:
       print("it is a leap year")
else:
   print("it is not a leap year")


#question 2
print("Enter length and breadth for a polygon :")
a,b=int(input()),int(input())
if a==b:
	print("it is a square")
else:
   	print("it is a rectangle")

#question 3
print("enter the age of three people")
x=int(input())
y=int(input())
z=int(input())
if  (x > y) & (x > z):
	print("1st person is oldest")
elif (y > x) & (y > z):	
    print("2nd person is oldest")
elif (z > x) & (z >y):
    print("3rd person is oldest")

if (x < y) & (x < z):
	print("1st person is youngest")
elif (y < x) & (y < z):	
    print("2nd person is youngest")
elif (z < x) & (z < y):
    print("3rd person is youngest")  
	
      
#question 4
print("enter age of a person:")
a=int(input())
print("enter your gender(M/F):")
s=input()
print("enter your martial status(Y/N):")
m=input()
if s == 'F':
   print("you can only work in urban areas")
elif (s =='M') & (a >= 20) & (a <= 40):
   print("you are elegible to work anywhere")
elif (s == 'M') & (a > 40) & (a <=60):
   print("you will work in urban areas")
else:
   print("Error:condition not satisfied")


#question 5
print("enter cost of the product:")
x=int(input())
if x > 1000:
   a=x-(0.10 * x)
   print("the cost after discount is:",a)
else:
   print("not aplicable for a discount")
     


#question 6
num=[]
for i in range(0, 10):
    c= int(input('Enter Number:'))
    num.append(c)
for i in range(10):
    print(num[i], end=' ')
print("\n")

#question 7
while True:
    print("infinite")

#question 8
num=[]
num1=[]
for i in range(0, 10):
    c= int(input('Enter Number:'))
    num.append(c)
for i in range(10):
    num1.append(num[i]*num[i])
    print(num1[i], end=' ')

#question 9
b=['prashant',23,12.6,'haldiyal',123.345,12]
ii=[]
s=[]
f=[]
v=len(b)
for i in range(v):
    if isinstance(b[i] , int):
       ii.append(b[i])
    elif isinstance(b[i] , float):
        f.append(b[i])
    elif isinstance(b[i] , str):
    	s.append(b[i])

print("\n")    	
for i in range(0, len(ii)):
    print(ii[i])
print("\n")    
for i in range(0, len(s)):
    print(s[i])
print("\n")    
for i in range(0, len(f)):           
    print(f[i])
    
#question 10
y= list()
for num in range(1, 101):
    p = True
    for i in range(2, num):
        if (num % i == 0):
            p = False
    if p:
        y.append(num)

l=len(y)      	
for i in range(0,l):
    print(y[i])

#question 11
j=0
for i in range(0,5):
    for j in range(0,i):
    	print("*",end='')
    print("\n")	

#question 12
f=[]
print("enter the size of a list:")
n=int(input())
print("enter the no. you want to search:")
y=int(input())
for i in range(0,n):
   c=int(input("enter a value:"))
   f.append(c)
for i in range(0,n):
   if f[i] == y:
      del f[i]
   print(f[i])            
