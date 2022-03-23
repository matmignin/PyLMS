#!/Users/matbook/.pyenv/versions/3.8.3/envs/VQenv/bin/python
import requests,datetime

headers = {
  'Authorization': 'pk_12858786_CAXE9O3ZDDOV31WBVR0S9D59W9CJEG0S',
  'Content-Type': 'application/json'
}
try:
  time_response = requests.get('https://private-anon-9bb174da19-clickup20.apiary-proxy.com/api/v2/team/8694610/time_entries/current?assignee=12858786', headers=headers)
  data= time_response.json()
  milliseconds = int(data['data']['duration'])
  task_name = data['data']['task']['name']

  seconds=str(int(-(milliseconds/1000)%60)).zfill(2)
  minutes=str(int(-(milliseconds/(1000*60))%60)).zfill(2)
  hours=str(int(-(milliseconds/(1000*60*60))%24))

  if milliseconds:
    if int(hours) > 1:
      time = hours + ':' + minutes
    else:
      time = minutes + ':' + seconds
    try:
      print(time + " — " + task_name)
    except:
      print('task_name')

except:
  print('^')






