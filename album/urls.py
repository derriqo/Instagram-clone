from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from instap import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('register/',views.registration, name ='register'),
    url('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name ='login'),
     url('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name ='logout'),
    url(r'',include('instap.urls')),
]