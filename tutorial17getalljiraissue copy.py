
import requests
from requests.auth import HTTPBasicAuth
import json

url="http://ashtan21.atlassian.net/rest/api/2/search"


headers = {
   "Accept": "application/json"
}

query = {
   'jql': 'project = ASHTAN'
}

response=requests.get(url,headers=headers,params=query,auth=("jhaashish21@gmail.com","zt4n9nzx1qOWhNLfAgFU903E"))
data=response.json()
issues=data["issues"]
for issue in issues:
    print(issue["key"])