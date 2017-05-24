from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import
# we are able to import from sibling directory using __init__.py,
#from SO; basically: putting a __init__.py file in a directory means
#  "in this directory, all of the .py files, and all of the subdirectories
#  which contain a __init__.py file, are part of the same package"

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('rango.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
