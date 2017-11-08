"""restproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from escuela.views import ApiEscuela, ApiEstudiante
from frontend.views import home_escuelas, home_estudiantes

urlpatterns = [
    url(r'^$', home_escuelas, name='home_escuelas'),
    url(r'^estudiantes/$', home_estudiantes, name='home_estudiantes'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/escuela/new', ApiEscuela.create),
    url(r'^api/escuela/$', ApiEscuela.get_all),
    url(r'^api/escuela/(?P<id_escuela>[0-9]+)/$', ApiEscuela.manage_by_id),
    url(r'^api/estudiante/new$', ApiEstudiante.create),
    url(r'^api/estudiante/$', ApiEstudiante.get_all),
    url(r'^api/estudiante/(?P<id_estudiante>[0-9]+)/$',
        ApiEstudiante.manage_by_id),
]
