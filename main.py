import requests
import datetime

TODAY = datetime.date.today()

GRAPH_ID = "test1"
pixela_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "aervapniervpa1"
USERNAME = "pablo96sies"
parameters = {"token": TOKEN,
              "username": USERNAME,
              "agreeTermsOfService": "yes",
              "notMinor": "yes"}

# response = requests.post(url=pixela_ENDPOINT, json=parameters)

#3 print(response.text)

graph_ENDPOINT = pixela_ENDPOINT + f"/{USERNAME}/graphs"
headers ={
    "X-USER-TOKEN": TOKEN}
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Gym",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}
# request = requests.post(url=graph_ENDPOINT, json=graph_parameters, headers=headers)
# print(request.text)

pix_ENDPOINT = graph_ENDPOINT + f"/{GRAPH_ID}"


TODAY_formated = str(TODAY).replace("-", "")
pix_parameters = {
    "date": TODAY_formated,
    "quantity": input("Did you go to the gym today? Write '1' if yes")
}
request = requests.post(url=pix_ENDPOINT, json=pix_parameters, headers=headers)
print(request.text)
update_parameters = {
    "quantity": "7"
}

update_ENDPOINT = f"{pix_ENDPOINT}/{TODAY_formated}"
# update = requests.put(url= update_ENDPOINT, json= update_parameters,headers= headers)

# delete = requests.delete(url= update_ENDPOINT, headers= headers)

#print(delete.text)