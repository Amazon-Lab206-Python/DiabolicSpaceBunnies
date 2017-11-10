from django.conf.urls import url, include
from . import views
url patterns = [
    url(r'^$', views.index)
]
