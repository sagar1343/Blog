from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('1/', views.yourposts, name='yourpost'),
    path('register/', views.register, name='register-page'),
    path('login/', views.login_user, name='login-page'),
    path('logout/', views.logout_user, name='logout-page'),
    path('profile/', views.profile, name='profile-page')
]
