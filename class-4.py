#question 1
pro=[23,'prashant',23.5,True,'Haldiyal',100,False]
for e in reversed(pro):
   print(e)

#question 2
print("\n")
s="iTs SunnY oUtsidE"
upper_s=""
for char in s:
	if char.isupper()==True:
		upper_s+=char
print(upper_s)

#question 3
print("enter numbers seperated by ,:")
n=input().split(',')
i=0
le = list(map(int,n))
for i in range(len(n)):
	le[i]=n[i]
l=int(len(le))
print(le[:l])

#question 4
n=input("enter a string:")
v=''.join(reversed(n))
if v == n:
	print("the string is palindrome")
else:
	print("the string is not palindrome")

#question 5
import copy
li=[1,23,4,5]
li2=copy.deepcopy(li)
li2[1]=0
print("li2=",li2[0:len(li2)])
print("li=",li[0:len(li)])
#diffrence between shallow and deepcopy
#A shallow copy means constructing a new collection object and then
#populating it with references to the child objects found in the original.
#In essence, a shallow copy is only one level deep.
#The copying process does not recurse and therefore won’t create copies of the child objects themselves.

#A deep copy makes the copying process recursive.
#It means first constructing a new collection object and then
#recursively populating it with copies of the child objects found in the original.
#Copying an object this way walks the whole object tree to create a fully independent clone of the original object and all of its children.
