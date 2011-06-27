from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from shop_simplevariations import urls as simplevariations_urls


urlpatterns = patterns('',
    # Example:
    #(r'^example/', include('example.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^shop/cart/', include(simplevariations_urls)),
    (r'^shop/', include('shop.urls')),
)