from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('instap.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', auth_views.logout, {"next_page": 'login'}, name='logout')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)