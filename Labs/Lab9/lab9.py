import json 
import requests 

r = requests.get('http://localhost:3000') 
data=r.json() 
i=0
color = ["blue", "green", "black"]
#word =str(color[0])
while i<len(data):
    print(data[i]['name'] + " is " + data[i]['color']) 
    i=i+1
