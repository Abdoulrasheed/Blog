from django.conf.urls import url, include
from django.contrib import admin
from blog.views import about, contact
from django.contrib.auth import views

urlpatterns = [
	url(r'^', include('blog.urls')),
    url(r'^about/abdul/$',about, name="about"),
    url(r'^contact/$',contact, name="contact"),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
]
