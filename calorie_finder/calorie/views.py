from django.shortcuts import render
from .forms import FoodCalorieForm
from django.contrib import messages
from django.http import JsonResponse
from calorie.models import Food_PercentValue

def index(request):
  search_result = {}
  if 'food' in request.POST:
    form = FoodCalorieForm(request.POST)
    if form.is_valid():
      search_result = form.search()
  else:
    form = FoodCalorieForm()
  return render(request, 'calorie/index.html', {'form': form, 'search_result': search_result})

  
  