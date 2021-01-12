'''
Created on Jan 12, 2021

@author: rkrap
'''
import json
import requests
from textwrap import indent
#r = requests.get('https://www.reddit.com/r/webdev.json')
r = requests.get('https://www.reddit.com/r/webdev.json', headers = {'User-agent': 'your bot 0.1'})

packages_json = r.json()
#print(packages_json)

packages_str = json.dumps(packages_json, indent=2)
print(packages_str)
