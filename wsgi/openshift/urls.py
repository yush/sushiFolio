from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'p55folio.views.home', name='home'),
    url(r'^fuel', 'p55folio.views.fuel', name='fuel'),
    url(r'^moire', 'p55folio.views.moire', name='moire'),
    url(r'^fractal', 'p55folio.views.fractal', name='fractal'),
    # url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
