from django import forms
from django.config import settings
import requests

class FoodCalorieForm(forms.Form):
  word = forms.CharField(max_length=100)

  def search(self):
    result={}
    word = self.cleaned_data['word']
    endpoint = ''
    url = endpoint.format(source_lang='en', word_id=word)
    headers={'app_id': settings.APP_ID, 'app_key': settings.APP_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200 #SUCCESS
      result = response.json()
      result['success'] = True
    else:
      result['success'] = False
      if response.status_code == 404 #NOT FOUND
        result['message'] = 'No entry found for "%s"' % word
      else:
        result['message'] = 'The EDAMAM API is not available at the moment. Please try again later.'
    return result