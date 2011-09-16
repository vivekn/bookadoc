from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookadoc.views.home', name='home'),
    # url(r'^bookadoc/', include('bookadoc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = patterns('bookadoc.app.views',
    url(r'^accounts/patients/registration/$', 'register_patient'),
    url(r'^accounts/doctors/registration/$', 'register_doctor'),
    url(r'^search/$', 'search'),
    url(r'^<?Pusername\S{1,30}>/appointments/$', 'appointments_index'),
    url(r'^<?Pusername\S{1,30}>/appointments/book/$', 'appointments_book'),
    url(r'^<?Pusername\S{1,30}>/appointments/cancel/$', 'appointments_cancel'),
    # This should come in the end
    url(r'^<?Pusername\S{1,30}>/$', 'index'),
)
