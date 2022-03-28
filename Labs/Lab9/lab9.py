import json 
import requests 

#pulling information from localhost of widget.js
r = requests.get('http://localhost:3000') 
#noting that the data needed for the print statement is within the data presented on the server
data=r.json() 
i=0
#list of colors needed in print statement
color = ["blue", "green", "black"]

#while statement that grabs data of each widget in the list and displays it
while i<len(data):
    print(data[i]['name'] + " is " + data[i]['color']) 
    i=i+1
