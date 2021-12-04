from django.contrib import admin
from django.urls import include, path
from django.urls.base import reverse_lazy
from django.urls.conf import re_path
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('app_software_development.urls')),
]
