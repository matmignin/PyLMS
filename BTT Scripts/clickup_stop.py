#!/Users/matbook/.pyenv/versions/3.8.3/envs/VQenv/bin/python
import requests,json

headers = {
  'Authorization': 'pk_12858786_CAXE9O3ZDDOV31WBVR0S9D59W9CJEG0S',
  'Content-Type': 'application/json'
}

stop_response = requests.post('https://api.clickup.com/api/v2/team/8694610/time_entries/stop', headers=headers)
