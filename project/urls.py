from django.urls import path
# from project.views import home_view, signup_view
# from django.conf import settings 
# from django.conf.urls.static import static 
from project import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^dashboard/$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^registration/$', views.Signup.as_view(), name='registration'),
    # url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    # url(r'^login/$', views.CustomLoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    # url(r'^registration/login/$', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    url(r'^login/$', views.CustomLoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^userlist/$', views.UserList.as_view(), name='userlist'),
    # url(r'^userlist/view/$', views.UserList.as_view(), name='userlist'),

]