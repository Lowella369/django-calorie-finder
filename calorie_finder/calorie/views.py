from django.shortcuts import render
from .forms import FoodCalorieForm

def food(request):
  search_result = {}
  if 'word' in request.GET:
    form = FoodCalorieForm(request.GET)
    if form.is_Valid()
      search_result = form.search()
  else:
    form = FoodCalorieForm()
  return render(request, 'templates/calorie/index.html', {'form': form, 'search_result': search_result})