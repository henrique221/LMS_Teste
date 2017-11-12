


from django.conf.urls import url
from app.views import home, login

urlpatterns = (
    url(r'^$', home, name='home'),
    url(r'^login/$', login, name='login')


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
