#question 1
print("enter values seperated with ',':")
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

#question 7
t=(1,3,4,5,67,9)
for i in range(1,len(t)+1):
    print(t[-i],end=" ")  

#question 8
j=0
min=max=t[0]
for j in range(0,len(t)):
	if t[j]<min:
		min=t[j]
	if t[j]>max:
		max=t[j]
print("\nlargest=",max)
print("\nsmallest=",min)		

#question 9
print("enter a string:")
s=input()
print(s.upper())

#question 10
print("enter a digit string:")
d=input()
print(d.isdigit())

#question 11
st="hello world"
s="prashant"
print(st.replace("world",s))

