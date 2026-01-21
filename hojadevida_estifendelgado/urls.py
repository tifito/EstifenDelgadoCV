"""
URL configuration for hojadevida_estifendelgado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from perfil import views  
# Archivos estáticos en DEBUG
from django.conf import settings
from django.conf.urls.static import static


# URL patterns principales
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cursos/', views.cursos, name='cursos'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('academico/', views.academico, name='academico'),
    path('laboral/', views.laboral, name='laboral'),
    path('garage/', views.garage, name='garage'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('cv-pdf/', views.cv_pdf, name='cv_pdf'),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
