#question 1
print("enter values seperated with ,")
li=input().split(',')
print(li[:len(li)])

#question 2
li=li+["‘google’","’apple’","’facebook’","’microsoft’","’tesla’"] 
print(li[:len(li)])

#question 3
print(li.count("1"))

#question 4
l2=[1,3,2,6,2,7,6,0]
l2.sort()
print("the sorted list is:",l2)   