import json
import requests
parameter={"cat":"movies","count":1}
response = requests.get("https://andruxnet-random-famous-quotes.p.mashape.com/",params=parameter)
data = response.json()
print(data)

