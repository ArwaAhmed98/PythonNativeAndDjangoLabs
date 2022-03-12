

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home , name='home'), #when hit /djapp/home => execute home() in View.py
    path('show/<st_id>', views.show ,name='show'),
    path('del/<st_id>' , views.stDEL,name='del'),
    path('st-add/' , views.stAdd , name='st-add'),
    path('st-edit/<st_id>' , views.stEdit , name='st-edit'),
    #rest apis ursl
    path('api-all', views.api_students_all, name='api-all'),
    path('api-show/<st_id>', views.api_students_show, name='api-show'),
    path('api-add', views.api_students_add, name='api-add'),
    path('api-edit/<st_id>', views.api_students_edit, name='api-edit'),
    path('api-del/<st_id>', views.api_students_del, name='api-del'),







]
