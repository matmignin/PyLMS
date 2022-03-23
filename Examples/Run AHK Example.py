import requests

headers = {
  'Authorization': 'pk_12858786_CAXE9O3ZDDOV31WBVR0S9D59W9CJEG0S',
  'Content-Type': 'application/json'
}
response = requests.get('https://private-anon-9bb174da19-clickup20.apiary-proxy.com/api/v2/team/8694610/time_entries/current?assignee=12858786', params=headers)

# response_body = urlopen(request).read()
print(response.json)




