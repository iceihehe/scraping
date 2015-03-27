from django.conf.urls import patterns, include, url
from django.contrib import admin
#from fetchcar.models import Car
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()
#admin.site.register(Car)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', "fetchcar.views.index"),
                       url(r'^fetchcar/', include('fetchcar.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )

urlpatterns += staticfiles_urlpatterns()
