#question 1
print("enter values seperated with ",":")
li=input().split(',')
print("the list entered is:")
print(li[:len(li)])

#question 2
print("the list after adding to the perivious list is:")
li=li+["‘google’","’apple’","’facebook’","’microsoft’","’tesla’"] 
print(li[:len(li)])

#question 3
z=li.count("1")
print("the count of 1 in list is:",z)

#question 4
l2=[1,3,2,6,2,7,6,0]
l2.sort()
print("the sorted list is:",l2)

#question 5
a=[1,3,5,7,2,9,3,1]
b=[2,9,1,3,6,3,1,0]
a.sort()
b.sort()
c=[]
c=a+b
c.sort()
print("the sorted array after mergeing is: ",c)

#question 6
x=y=0
for i in range(0,len(c)):
	if c[i]%2 ==0:
		x=x+1
	else:
	    y=y+1

print("the number of odd and even numbers in above list is:")
print("even :",x)
print("odd :",y)	    	
   