from django.contrib import admin
from django.urls import path
from . import views

# Gambar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/',views.profile,name='profile'),
    path('forms/',views.create_risk,name='forms'),
    path('tabel/',views.tabel,name='tabel'),
    path('edit/<int:id>/', views.edit_risk, name='edit_risk'),
    path('delete/<int:id>/', views.delete_risk, name='delete_risk'),
    path('risiko/<int:risk_id>/', views.risk_detail, name='risk_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #load gambar
