from django import forms
from django.conf import settings
import requests
from urllib.parse import urlencode
from django.contrib import messages
from calorie.models import Food_PercentValue

class FoodCalorieForm(forms.Form):
  food = forms.CharField(max_length=100)

  def search(self):
    result = {}
    food = self.cleaned_data['food']
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    headers = {'x-app-id': settings.APP_ID, 'x-app-key': settings.APP_KEY, 'x-remote-user-id': '0', 'content-type': 'application/x-www-form-urlencoded'}
    payload = urlencode({'query': food})
    response = requests.post(url, headers=headers, data=payload)

    if response.status_code== 200:
      result = response.json()
      result['success'] = True
      data = result['foods']
      food_data = data[0]
      context = {
        'name': food_data['food_name'],
        'img': food_data['photo'],
        'serving_qty': food_data['serving_qty'],
        'serving_unit': food_data['serving_unit'],
        'calories': food_data['nf_calories'],
        'total_fata': food_data['nf_total_fat'],
        'sat_fat': food_data['nf_saturated_fat'],
        'cholesterol': food_data['nf_cholesterol'],
        'sodium': food_data['nf_sodium'],
        'total_carbohydrate': food_data['nf_total_carbohydrate'],
        'dietary_fiber': food_data['nf_dietary_fiber'],
        'sugar': food_data['nf_sugar'],
        'protein': food_data['nf_protein'],
        'calories_daily_percent': round(food_data['nf_calories'] / Food_PercentValue.rec_calorieIntake * 100, 2),
        'fat_daily_percent': round(food_data['nf_total_fat'] / Food_PercentValue.rec_dailyValueTotalFat * 100, 2),
        'sat_fat_daily_percent': round(food_data['nf_saturated_fat'] / Food_PercentValue.rec_dailyValueSatFat * 100, 2),
        'cholesterol_daily_percent': round(food_data['nf_cholesterol'] / Food_PercentValue.rec_dailyValueCholesterol * 100, 2),
        'sodium_daily_percent': round(food_data['nf_sodium'] / Food_PercentValue.rec_dailyValueSodium * 100, 2),
        'carbs_daily_percent': round(food_data['nt_total_carbohydrate'] / Food_PercentValue.rec_dailyValueCarbo * 100, 2),
        'fiber_daily_percent': round(food_data['nf_dietary_fiber'] / Food_PercentValue.rec_dailyValueFiber * 100, 2),
        'sugar_daily_percent': "N/A",
      }
      return context
    else:
      result['success'] = False
      if response.status_code == 400:
        result['message'] = "%s" % food + " is not found in the API Database"
      else:
        result['message'] = "API Server is not available at the momenet. Try again Later."
    return result




		
