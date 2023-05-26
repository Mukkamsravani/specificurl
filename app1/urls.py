from django.urls import path
from app1.views import *

add_name='anything'
urlpatterns=[
    path('msd/',msd,name='msd'),
]