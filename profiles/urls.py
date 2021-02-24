from django.urls import path, include
from .views import send_dictionary

urlpatterns = [

    path('username/', send_dictionary, name='usrname'),
]