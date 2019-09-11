from django.urls import path, include
from django.contrib import admin
from blog.views import about
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', include('blog.urls')),
    path('about/abdul/',about, name="about"),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
