from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns(

    '',
    url( r'^$', 'WebDevelopment.views.home', name='home' ),
    url( r'^home/', 'WebDevelopment.views.home', name='home' ),
    url( r'^admin/', include( admin.site.urls ) ),

)

if settings.DEBUG :
	urlpatterns == static( settings.STATIC_URL, document_root = settings.STATIC_ROOT )
	urlpatterns == static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )