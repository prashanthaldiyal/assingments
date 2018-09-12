#question 1
dictonary={'name':'prashant','branch':'computer-science','course':'B.Tech'}
for key,value in dictonary.items():
	print(key,'is the key for the value',value)

#question 2
dict1={'sam':{'maths':'50','science':'88','physics':'90'},'geeta':{'maths':'60','science':'80','physics':'70'}}   
for name, sub in dict1.items():  
    print("\nname:", name)       
    for key in sub:
        print(key +':', sub[key])
