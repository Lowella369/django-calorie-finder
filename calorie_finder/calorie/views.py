from django.shortcuts import render
from .forms import FoodCalorieForm

def index(request):
  search_result = {}
  if 'food' in request.GET:
    form = FoodCalorieForm(request.GET)
    if form.is_valid():
      search_result = form.search()
  else:
    form = FoodCalorieForm()
  return render(request, 'calorie/index.html', {'form': form, 'search_result': search_result})