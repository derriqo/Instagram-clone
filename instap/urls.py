from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.mwanzo, name='first-page'),
    url(r'register/',views.registration,name='register'),
    url(r'^search/',views.search_users, name='search_users'),
    url(r'^profile',views.profile,name='profile'),
]




