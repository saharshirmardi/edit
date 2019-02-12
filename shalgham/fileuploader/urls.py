from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('upload/ss/', views.siasefid, name='ss'),
    path('upload/cr/', views.crop, name='cr'),
    path('upload/rt/', views.rotate, name='rt'),
    path('upload/rs/', views.resize, name='rs'),
    path('admin/', admin.site.urls),
    path('upload/back/', views.back, name='bck'),
    path('upload/share/', views.share, name='shr')
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
