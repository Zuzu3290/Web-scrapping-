import requests
import json

response = requests.get("")  #th relevant Api link or https link need to be placed for the applctaion to receiev data 

for data in response.json():  #json method is used to convert the response into json format
#
# for data in response.json()['items']:
#then we save or print data via iterations
#cleaninig also or preprocessing takes place here for example : if[data] == 0: