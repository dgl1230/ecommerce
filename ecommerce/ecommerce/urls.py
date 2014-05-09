from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  	url(r'^$', 'products.views.list_all_products', name="all_products"),
  	url(r'^cart/', include('carts.urls')),
	url(r'^products/', include('products.urls')),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
		{'document_root': settings.STATIC_ROOT}), 
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
		{'document_root': settings.MEDIA_ROOT}), 
    url(r'^admin/', include(admin.site.urls)),
)
