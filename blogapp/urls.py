from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='user/', view=views.yourposts, name='yourpost'),
    path(route='register/', view=views.register, name='register-page'),
    path(route='login/', view=views.login_user, name='login-page'),
    path(route='logout/', view=views.logout_user, name='logout-page'),
    path(route='profile/', view=views.profile, name='profile-page'),
    path(route='create/', view=views.createBlog, name='createBlog')
]
