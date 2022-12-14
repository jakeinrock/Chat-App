from django.contrib.auth import views as auth_views
from django.urls import path

from room import views as room_views
from . import views


urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('create/', room_views.createroom, name='create'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
