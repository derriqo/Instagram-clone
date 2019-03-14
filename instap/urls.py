from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^$',views.registration, name='register'),
    url('^search/',views.search_users, name='search_users'),
    url('^login/$', auth_views.login,name='login'),
    url('^create/$', views.createPost,name='create'),
    url('^index/$', views.index, name='index'),
    url('^signout/$', views.signout, name='signout'),
    url('^profile/',views.profile,name='profile'),
]