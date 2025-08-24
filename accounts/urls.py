from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),
    path('update_profile', views.upate_profile_view, name='update_profile'),
]