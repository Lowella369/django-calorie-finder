from django import forms
from django.conf import settings
import requests
from urllib.parse import urlencode

class FoodCalorieForm(forms.Form):
  food = forms.CharField(max_length=100)

  def search(self):
    result={}
    food = self.cleaned_data['food']
    url = urlencode('https://api.edamam.com/api/food-database/parser?ingr=' % food)
    headers={'app_id': settings.APP_ID, 'app_key': settings.APP_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
      result = response.json()
      result['success'] = True
    else:
      result['success'] = False
      if response.status_code == 404:
        result['message'] = 'No entry found for "%s"' % word
      else:
        result['message'] = 'The EDAMAM API is not available at the moment. Please try again later.'
    return result