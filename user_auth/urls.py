from django.urls import path
from user_auth import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^dashboard/$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^registration/$', views.Signup.as_view(), name='registration'),
    url(r'^login/$', views.CustomLoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^userlist/$', views.UserList.as_view(), name='userlist'),

]