from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings  # New Import
from registration.backends.simple.views import RegistrationView
from django.conf.urls.static import static # New Import


# we are able to import from sibling directory using __init__.py,
#from SO; basically: putting a __init__.py file in a directory means
#  "in this directory, all of the .py files, and all of the subdirectories
#  which contain a __init__.py file, are part of the same package"


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/'


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('rango.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
