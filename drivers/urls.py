from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.d_index,name='driverindex'),
    # url(r'^$', views.d_homepage,name='driverhome'),
    url(r'^about/$', views.about,name='about'),
    url(r'^profiles/(?P<username>[-_\w.]+)$',views.profile,name='profiles'),
    url(r'^profiles/edit/(?P<username>[-_\w.]+)$', views.update_profile,name='editprofile'),
]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
