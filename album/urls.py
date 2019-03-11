from django.conf.urls import url,include
from django.contrib import admin
from instap import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('register/',views.registration, name ='register'),
    url(r'',include('instap.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]