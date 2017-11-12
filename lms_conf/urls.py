"""
Definition of urls for django_get_started.
"""


from django.conf.urls import url
from lms_app import views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

urlpatterns = (
    # Examples:
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home')
)

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

