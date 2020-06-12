import os
import requests

def get_food():
	url=''
  r = requests.get(url, headers={'Authorization':'Bearer %s' % 'access_token'})
  food = r.json()
  food_list = []
for i in range(len(food[])):
	food_list.append(food[][i])
return food_list
