from django.contrib import admin
from django.urls import path
from . import views

# Gambar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('profile/',views.profile,name='profile'),
    path('signup/',views.signup,name='signup'),
    path('forms/',views.forms,name='forms'),
    path('tabel/',views.tabel,name='tabel'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('chart/',views.chart,name='chart')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #load gambar

hander404 = "views.handler404"
