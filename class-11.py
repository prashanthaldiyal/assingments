#question 1
import re
text="my name is prashant and my email address is prashant26haldiyal@gmail.com"
email=re.search(r'[\w\.*]+@[\w\.*]+',text)
print(email)

#question 2
text="my name is prashant and my phone no.rs are +91-7060733805,+91-6123245656"
phone=re.findall(r'[+91-]+[6-9]+[0-9]{9}',text)
print(phone)