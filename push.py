import json
import requests
from datetime import datetime

api = 'https://push.i-i.me'
push_key = 'LU8BoRGBXBqev27Qhk9m'
title = 'Test Push'
content = 'hello world'


def send_push(push_key, title, content, type='text', current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
    headers = {'Content-Type': 'application/json'}
    json_data = {
      "push_key": push_key,
      "title": title,
      "content": content,
      "type": type,
      "date": current_time  
    }

    response = requests.post(api, headers=headers, data=json.dumps(json_data))

    if response.status_code == 200:
      print('Push sent successfully.')
    else:
      print('Push failed. Error:', response.text)

if __name__ == '__main__':
    send_push(push_key, title, content,)

