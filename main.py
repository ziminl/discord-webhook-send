


import requests
import json
webhookurl = 'webhookurl'
data = {
  'content': 'text',
  'username': 'username',
  "avatar_url": "https://i.imgur.com/oBPXx0D.png"
}

# Send the webhook message
response = requests.post(webhookurl, json=data)

if response.status_code == 204:
    print('Sent')
else:
    print('Error:', response.status_code)
