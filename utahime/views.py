from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import S_Idol
# Create your views here.

class utahime(TemplateView):

    def get(self, request):
        return render(request, 'utahime/index.html')

class CardList(TemplateView):

    def get(self, request):
        params = {
            'scard': S_Idol.objects.all()
        }
        return render(request, 'utahime/cardlist.html',params)
