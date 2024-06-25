import requests
import json
import base64
import re
while True:
	name= input("Enter the pull request ID:: ")
	pat = 'f7xp6dlcjgw7rhphw5yzrh2ntpla6qappy2b7qjiknzcgv4nneqq'
	authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')
	headers = {
     	    'Accept': 'application/json',
     	    'Authorization': 'Basic '+authorization
	}
	response = requests.get(
    	    url="https://dev.azure.com/singhramnik111/c6dd43da-daec-48d8-a5f9-27f11dfebba6/_apis/git/repositories/87c4405d-b122-4b60-a9f5-3c603d9d2b95/pullRequests/" + name,  headers=headers)
	data= response.json()
	data75= (len(data))
	if data75 > 8:
		break
	else:
		print("YOU HAVE MENTIONED INCORRECT ID.. PLEASE TRY AGAIN!\n")


title=data["title"]
description=data["description"]

data10= (len(title))

while True:
        if data10 == 17:
                print("\n ============================================================ \n THE TITLE " + title + " IS CORRECT \n ============================================================")
                break
        else:
                print("============================================================ \n THE TITLE " + title + " IS INNCORRECT \n ============================================================")
                break

special= re.compile('#')

if(special.search(description) == None):
	print("DESCRIPTION:: \n" + "\n" + description + "\n ============================================================")
else:
        print("DESCRIPTION:: \n" + "\n" + description + "\n" + "\n NOTE= YOU HAVE MENTIONED THE # SO IF YOU DON'T NEED THEN PLEASE EDIT THE DESCRIPTION AND REMOVE IT \n ============================================================")


pat = 'f7xp6dlcjgw7rhphw5yzrh2ntpla6qappy2b7qjiknzcgv4nneqq'
authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')
headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic '+authorization
}
response = requests.get(
    url="https://dev.azure.com/singhramnik111/c6dd43da-daec-48d8-a5f9-27f11dfebba6/_apis/git/repositories/87c4405d-b122-4b60-a9f5-3c603d9d2b95/pullRequests/" + name  + "/workitems",  headers=headers)
data55= response.json()

data77=data55["value"]

count=data55["count"]


if count == 1:
	data78= (str(data77))
	x = data78.split()
	data79= (x[3])
	data81= data79.replace("'", "").replace("}","").replace("]","")
	pat = 'f7xp6dlcjgw7rhphw5yzrh2ntpla6qappy2b7qjiknzcgv4nneqq'
	authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')
	headers = {
		'Accept': 'application/json',
		'Authorization': 'Basic '+authorization
	}
	response = requests.get(
		url=data81,  headers=headers)
	data60= response.json()
	data61=(data60["fields"])
	data62=(data61["System.WorkItemType"])
	print("THE WORK ITEM TYPE IS " + data62 + "\n ============================================================")		
else:
	print("THE WORK ITEM HAS NOT ATTACHED \n ============================================================")


