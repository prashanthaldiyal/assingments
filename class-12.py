#question 1
from datetime import date
today=date.today()
print("today's date is:",today.day,today.month,today.year)
#question 2
import webbrowser as w
url="https://www.youtube.com/watch?v=cpPG0bKHYKc"
w.open(url)

#question 3
import os
from os import path
op=path.realpath("p2.txt")
os.rename('p2.txt','p21.jpg')
print("the file is changed")

