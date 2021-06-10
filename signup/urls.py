from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logoutUser, name='lougout')
]