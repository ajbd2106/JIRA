import requests
import json
import io
url="http://ashtan21.atlassian.net/rest/api/2/search"
headers={
  "Accept": "application/json",
    "Content-Type": "application/json"
}

query = {
   'jql': 'project = ASHTAN'
}

response=requests.get(url,headers=headers,params=query,auth=("jhaashish21@gmail.com","zt4n9nzx1qOWhNLfAgFU903E"))
print(response.text)
