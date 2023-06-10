from django.urls import path
from . import views
app_name = 'app0'
urlpatterns = [
    path('',  views.static, name='stat'),
    path('temp/', views.templates, name = 'templates')
   #  path('', views.demo, name='demo'),
   #  path('add/', views.add, name='add')
   # path('about/', views.about, name='about'),
   #  path('contacts/', views.contact)
]
