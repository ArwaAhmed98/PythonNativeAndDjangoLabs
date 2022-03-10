

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home , name='home'), #when hit /djapp/home => execute home() in View.py
    path('show/<st_id>', views.show ,name='show'),
    path('del/<st_id>' , views.stDEL,name='del')



]
