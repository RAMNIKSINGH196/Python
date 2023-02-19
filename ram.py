import requests
import json
import base64
while True:
	name= input("Enter the pull request ID: ")
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
                print("THE TITLE " + title + " IS CORRECT\n")
                break
        else:
                print("THE TITLE " + title + " IS INNCORRECT\n")
                break

data11= (len(description))

while True:
        if data11 > 1:
                print("FOLLOWING IS THE DESCRIPTION\n", description + "\n")
                break
        else:
                print("YOU HAVE NOT MENTIONED THE DESCRIPTION\n")
                break
#name1= workitems
pat = 'f7xp6dlcjgw7rhphw5yzrh2ntpla6qappy2b7qjiknzcgv4nneqq'
authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')
headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic '+authorization
}
response = requests.get(
    url="https://dev.azure.com/singhramnik111/c6dd43da-daec-48d8-a5f9-27f11dfebba6/_apis/git/repositories/87c4405d-b122-4b60-a9f5-3c603d9d2b95/pullRequests/" + name  + "workitems",  headers=headers)
data55= response.json()

count=data55["count"]

while True:
        if count == 1:
                print("THE WORK ITEM HAS BEEN ATTACHED\n")
                break
        else:
                print("THE WORK ITEM HAS NOT ATTACHED\n")
                break

