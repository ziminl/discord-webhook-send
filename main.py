


import requests
import json
webhookurl = 'webhookurl'
payload = {
  'content': 'text',
  'username': 'username',
  'avatar_url': 'https://en.wikipedia.org/wiki/File:Test-Logo.svg'
}

# Send the webhook message
response = requests.post(webhookurl, json=payload)

if response.status_code == 204:
    print('sent')
else:
    print('error:', response.status_code)



