from django.urls import path
from django.urls.conf import re_path
from .views import RegisterFormView, redirect_view


urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    re_path(r'.*', redirect_view, name='redirect'),
]
