from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
	url(r'^', include('blog.urls')),
    url(r'^about/abdul/$',views.about, name="about"),
    url(r'^contact/$',views.contact, name="contact"),
    url(r'^admin/', admin.site.urls),
]
