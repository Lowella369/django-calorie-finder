from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class GetCalorie(TemplateView):
    template_name = 'calorie/index.html'
    def get_context_data(self, *args, **kwargs):
        pass