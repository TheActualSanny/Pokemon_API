from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthenticationHomeView.as_view(), name = 'authenticate-home'),
    path('register/', views.Register.as_view(), name = 'register'),
    path('login/', views.Login.as_view(), name = 'login')
]