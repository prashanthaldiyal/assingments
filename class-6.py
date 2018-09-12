#question 1
def area(r):
    a=4*3.14*r*r
    print("area of sphere is:",a)
print("enter radius of a sphere:")
r=float(input())
area(r)

#question 2
def perfect(n):
    
    i=0
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")
    for c in range(1,1000):
        if sum(x for x in range(1,c) if not c%x)==c:
            print(c)


n = int(input("Enter any number: "))
perfect(n)

#question 3
print("enter a number:")
n=int(input())
for i in range(1,11):
    print(str(i)+"*"+str(n)+"="+str(n*i))

#question 4
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print(power(base,exp))