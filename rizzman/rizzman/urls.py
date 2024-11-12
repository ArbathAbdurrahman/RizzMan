from django.contrib import admin
from django.urls import path
from . import views

# Gambar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #load gambar
