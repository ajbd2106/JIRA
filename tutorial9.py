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
data=response.json()
issues=data["issues"]
for issue in issues:
    issue_key=issue["key"]
    url1="http://ashtan21.atlassian.net/rest/api/2/issue/"+issue_key
    response=requests.get(url1,headers=headers,auth=("jhaashish21@gmail.com","zt4n9nzx1qOWhNLfAgFU903E"))
    data=response.json()
    print(f'issue id is {issue_key} and status is {data["fields"]["status"]["name"]}')



