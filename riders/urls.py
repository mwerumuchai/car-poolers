from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'riders'

urlpatterns = [
    url(r'^$', views.r_index,name='riderindex'),
    url(r'^about/$', views.about,name='about'),
    url(r'^profiles/(?P<username>[-_\w.]+)/$', views.profile,name='riderprofiles'),
    url(r'^profiles/edit/(?P<username>[-_\w.]+)/$', views.update_profile,name='edit'),
    url(r'^profiles/driverprofile/(\d+)/$', views.driverprofile, name='driverprofile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
