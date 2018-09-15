#question 1
#a=3
#if a < 4:
#   a=a/(a-3)
#print(a)
#output
#the exception occured is ZeroDivisionError: integer division or modulo by zero
#solution
try:
	a=3
	if a<4:
		a=a/(a-3)
	print(a)
except ZeroDivisionError:
    print("number cannot be divisile by zero")				
else:
    a=4
    if a<4:
    	a=a/(a-3)  
    print(a)
    
#question 2
#l=[1,2,3]
#print(l[3])
# the error is IndexError: list index out of range
#solution
l=[1,2,3]
print(l[0:3])

#question 3
#try:
#    raise NameError("Hi there")
#except NameError:
#    print("An exception")
#    raise
#output:--
#An exception
#Traceback (most recent call last):
#  File "class-8.py", line 18, in <module>
#    raise NameError("Hi there")
#NameError: Hi there

#question 4
def AbyB(a,b):
   try:
       c=((a+b)/(a-b))
   except ZeroDivisionError:
       print("a/b result in 0")
   else:
       print(c)
AbyB(2.0,3.0)
AbyB(3.0,3.0)
#output
#-5.0
#a/b result in 0


#question 5

#l=[1,2,3]
#print(l[3])
#output
# the error is IndexError: list index out of range
#solution
l=[1,2,3]
print(l[0:3])


#import package
#print(package)
#because package is not defined
#ImportError: No module named package
import sys
print(sys)

#int("prashant")
#output
#ValueError: invalid literal for int() with base 10: 'prashant'
#solution
int(5)


