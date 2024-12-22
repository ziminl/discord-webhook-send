
import requests
import json

webhookurl = 'webhookurl'

requests.post(webhookurl, json={'content': 'text2change', 'username': 'username2change', 'avatar_url': 'https://i.imgur.com/oBPXx0D.png'}) 
