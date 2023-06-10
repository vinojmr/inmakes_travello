from django.urls import path, include
from . import views
from project0 import settings

urlpatterns = [
    path('log/', views.log, name='log'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('html/', views.html, name='html'),
]