from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.mwanzo, name='first-page'),

    url(r'register/',views.registration,name='register'),
]