from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'drivers'

urlpatterns = [
    url(r'^$', views.d_index,name='driverindex'),
    url(r'^about/$', views.about,name='about'),
    url(r'^profiles/(?P<username>[-_\w.]+)/$', views.profile,name='driverprofile'),
    url(r'^profiles/edit/(?P<username>[-_\w.]+)/$', views.update_profile,name='edit'),
    url(r'^profiles/car/(?P<username>[-_\w.]+)/$', views.car, name='cardetails'),
    url(r'^profiles/riderprofile/(\d+)/$', views.riderprofile, name='riderprofile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
