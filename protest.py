import requests
import json
import re
request_name=input("Enter your name:")
data = []
data3 = []
request1 = ['configui', 'hue', 'qubole', 'openvpn', 'looker', 'redash']
env1= ['aws-prod', 'aws-cs', 'aws-eu-prod', 'aws-eu-cs', 'gcp-prod', 'gcp-cs', 'qa', 'dev', 'internal']
configuiappro1= ['ryan.garaygay', 'brian.liao' , 'sevgi.cavusyan' , 'barrett.smith', 'harshit.sharma', 'meagen.williams', 'suyash.jain', 'simon.elliott', 'brittany.minnehan', 'lisa.Campopiano', 'rockie.teo', 'tushar.gupta', 'ashish.agarwal', 'allen.chan', 'harshit.sharma', 'raghu.bishnoi', 'brianna.mccullough']
configuiappro2=['ryan.garaygay', 'brian.liao' , 'sevgi.cavusyan' , 'barrett.smith', 'harshit.sharma', 'meagen.williams', 'suyash.jain', 'simon.elliott', 'brittany.minnehan', 'lisa.Campopiano', 'rockie.teo', 'tushar.gupta', 'ashish.agarwal', 'allen.chan', '"harshit.sharma', 'raghu.bishnoi', 'brianna.mccullough']
configuiappro3= ['ryan.garaygay', 'ashish.agarwal', 'suyash.jain', 'allen.chan', 'harshit.sharma']
hue1= ['allen.chan', 'suyash.jain', 'ashish.agarwal', 'harshit.sharma']
hue2= ['brian.liao', 'allen.chan', 'ashish.agarwal', 'harshit.sharma']
qubole1= ['brian.liao', 'arnaud.prades', '61f6347fb3ec760068b0aa10']
qubole2= ['brian.liao', 'chinmay.vaidya', 'arnaud.prades', 'meagen.williams']
openvpn1= ['sevgi.cavusyan', 'barrett.smith', 'rockie.teo', 'tushar.gupta', 'ashish.agarwal', 'brian.liao', 'meagen.williams', 'suyash.jain', 'harshit.sharma']
openvpn2= ['allen.chan', 'ashish.agarwal', 'brian.liao', 'harshit.sharma']
openvpn3= ['allen.chan', 'ashish.agarwal', 'harshit.sharma']
looker1= ['mukesh.malhotra', 'saket.gupta']
redash1= ['allen.chan', 'jim.idelson', 'brian.liao', 'sevgi.cavusyan', 'barrett.smith', 'meagen.williams', 'suyash.jain', 'simon.elliott', 'ashish.agarwal', 'rockie.teo', 'tushar.gupta', 'harshit.sharma', 'raghu.bishnoi']

while True:
	request_email=input("Enter the request email address:")
	data.append(request_email)
	tenant=input("please enter the tenant:")
	data.append(tenant)
	role=input("please enter the role:")
	data.append(role)
	print(f"Hello {request_name} please choose following request")
	print(request1)
	while True:
		request=input("please enter above mentioned request:")
		if (request.casefold() not in request1):
			print("Sorry You have mentioned inncorrect request.")
		else:
			data.append(request)
			break
	while True:
		env=input(f"please enter the one of this mentioned env {env1}:")
		if (env.casefold() not in env1):
			print("Sorry You have mentioned inncorrect envid.")
		else:
			data.append(env)
			break
	if (request.casefold() in "configui" and env.casefold() in "aws-prod") or (request.casefold() in "configui" and env.casefold() in "aws-eu-prod") or (request.casefold() in "configui" and env.casefold() in "gcp-prod"):
		print(f"""For configui prod env choose one of the following Approver.
			{configuiappro1}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for configui prod env:")
			if (approvername.casefold() not in configuiappro1):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	elif (request.casefold() in "configui" and env.casefold() in "aws-cs") or (request.casefold() in "configui" and env.casefold() in "aws-eu-cs") or (request.casefold() in "configui" and env.casefold() in "gcp-cs"):
		print(f"""For configui cs env choose one of the following Approver.
			{configuiappro2}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for configui cs env:")
			if (approvername.casefold() not in configuiappro2):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	elif (request.casefold() in "configui" and env.casefold() in "dev") or (request.casefold() in "configui" and env.casefold() in "qa"):
		print(f"""For configui qa or dev env choose one of the following Approver.
			{configuiappro3}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for configui qa or dev env:")
			if (approvername.casefold() not in configuiappro3):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	elif (request.casefold() in "hue" and env.casefold() in "dev") or (request.casefold() in "hue" and env.casefold() in "qa") or (request.casefold() in "hue" and env.casefold() in "aws-cs")  or (request.casefold() in "hue" and env.casefold() in "aws-eu-cs") or (request.casefold() in "hue" and env.casefold() in "gcp-cs"):
		print(f"""For hue qa or dev or cs env choose one of the following Approver.
			{hue1}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for hue qa or dev or cs env:")
			if (approvername.casefold() not in hue1):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	elif (request.casefold() in "hue" and env.casefold() in "aws-prod") or (request.casefold() in "hue" and env.casefold() in "aws-eu-prod") or (request.casefold() in "hue" and env.casefold() in "gcp-prod"):
		print(f"""For hue prod env choose one of the following Approver.
			{hue2}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for hue prod env:")
			if (approvername.casefold() not in hue2):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	elif (request.casefold() in "qubole" and env.casefold() in "aws-prod") or (request.casefold() in "qubole" and env.casefold() in "aws-eu-prod") or (request.casefold() in "qubole" and env.casefold() in "gcp-prod"):
		print(f"""For qubole prod env choose one of the following Approver.
			{qubole1}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for qubole prod env:")
			if (approvername.casefold() not in qubole1):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	elif (request.casefold() in "qubole" and env.casefold() in "aws-cs") or (request.casefold() in "qubole" and env.casefold() in "aws-eu-cs") or (request.casefold() in "qubole" and env.casefold() in "gcp-cs"):
		print(f"""For qubole cs env choose one of the following Approver.
			{qubole2}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for qubole cs env:")
			if (approvername.casefold() not in qubole2):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	elif (request.casefold() in "openvpn" and env.casefold() in "aws-cs") or (request.casefold() in "openvpn" and env.casefold() in "aws-eu-cs") or (request.casefold() in "openvpn" and env.casefold() in "gcp-cs"):
		print(f"""For openvpn cs env choose one of the following Approver.
			{openvpn1}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for openvpn cs env:")
			if (approvername.casefold() not in openvpn1):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	elif (request.casefold() in "openvpn" and env.casefold() in "aws-prod") or (request.casefold() in "openvpn" and env.casefold() in "aws-eu-prod") or (request.casefold() in "openvpn" and env.casefold() in "gcp-prod"):
		print(f"""For openvpn prod env choose one of the following Approver.
			{openvpn2}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for openvpn prod env:")
			if (approvername.casefold() not in openvpn2):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	elif (request.casefold() in "openvpn" and env.casefold() in "qa") or (request.casefold() in "openvpn" and env.casefold() in "dev"):
		print(f"""For openvpn dev or qa env choose one of the following Approver.
			{openvpn3}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for openvpn qa or dev env:")
			if (approvername.casefold() not in openvpn3):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	elif (request.casefold() in "looker" and env.casefold() in "aws-cs") or (request.casefold() in "looker" and env.casefold() in "aws-eu-cs") or (request.casefold() in "looker" and env.casefold() in "gcp-cs") or (request.casefold() in "looker" and env.casefold() in "aws-prod") or (request.casefold() in "looker" and env.casefold() in "aws-eu-prod") or (request.casefold() in "looker" and env.casefold() in "gcp-prod"):
		print(f"""For looker prod or cs env choose one of the following Approver.
			{looker1}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for looker prod or cs env:")
			if (approvername.casefold() not in looker1):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	elif (request.casefold() in "redash" and env.casefold() in "aws-prod") or (request.casefold() in "redash" and env.casefold() in "aws-eu-prod") or (request.casefold() in "redash" and env.casefold() in "gcp-prod") or (request.casefold() in "redash" and env.casefold() in "internal"):
		print(f"""For redash prod or internal env choose one of the following Approver.
			{redash1}""")
		while True:
			approvername=input("please enter above mentioned Approver Name for redash prod or internal env:")
			if (approvername.casefold() not in redash1):
				print("Sorry You have mentioned inncorrect Approver.")
			else:
				approvername= ("[" + "~" + approvername + "]")
				data.append(approvername)
				break
	else:
		print("You have choose incorrect env according to request so please again enter the correct env")
		exit()
	choice = input("Enter Another request email address ?? ( y / n ) :")
	if choice.casefold() == 'n':
		break


data5 = ['request email address-', 'tenant-', 'role-', 'request-', 'env-', 'Approver-']
m_input = len(data)
data6 = m_input/6
data7 = (int(data6))
data8 = data7*data5
data10 = []

for element in range(len(data8)):
	data9= (data8[element], data[element])
	data10.append(data9)

data11 = (str(data10))

special="(,''"
for i in special:
	data11=data11.replace(i,"")
print(data11)

data12 = re.sub('\)', "\n",data11)
print(data12)
print(type(data12))


url = "https://ramnik196.atlassian.net/rest/api/2/issue"
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
payload=json.dumps(
   {
    "fields": {
       "project":
       {
          "key": "RAMNIKS"
       },
       "summary": request,
       "description": data12,
       "components": [
        {
         "name": "access"
        }
       ],
       "issuetype": {
          "name": "Task"
       },
       "labels": [
       "access_request"
       ]
   }
}
)
response=requests.post(url,headers=headers,data=payload,auth=("singhramnik111@gmail.com","xNTwiptw6Wx84nWDtPYOFC51"))
print(response.text)
file= open('response.text', 'w')
file.write(response.text)
file.close()

