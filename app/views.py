from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from app.models import *
# Create your views here.

class Home(TemplateView):
    template_name='app/home.html'

class Trainer_list(ListView):
    model=Trainer
    context_object_name='trainers'
    #queryset=Trainer.objects.filter(name='Santhosh')
    #ordering=['name']

class Detail(DetailView):
    model=Trainer
    context_object_name='tr'