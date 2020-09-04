from django.urls import path
from utahime.views import utahime, CardList

urlpatterns = [
    path('', utahime.as_view(), name = 'index'),
    path('cardlist', CardList.as_view(), name='cardname'),
]
