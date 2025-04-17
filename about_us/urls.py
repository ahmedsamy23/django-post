from nturl2path import url2pathname
from django import urls
from django.urls import URLPattern, path
from . import views

app_name = 'about_us'

urlpatterns = [
    path('about/' , views.AboutView.as_view() , name='about'),
]
