from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('blog_admin/', admin.site.urls),
    path('', views.blog_index, name='blog_home'),
]
