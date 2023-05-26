from django.urls import path
from app2.views import *

add_name='something'
urlpatterns=[
    path('virat/',virat,name='virat'),
]