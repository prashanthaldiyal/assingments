#question 1
from datetime import date
today=date.today()
print("today's date is:",today.day,today.month,today.year)

#question 3
import os
from os import path
op=path.realpath("p2.txt")
os.rename('p2.txt','p21.jpg')
print("the file is changed")

