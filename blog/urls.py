from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', views.user_login, name='blog-login'),
    path('register/', views.user_register, name='blog-register'),
]