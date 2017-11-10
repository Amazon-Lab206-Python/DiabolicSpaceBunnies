from django.conf.urls improt url, include
from . import views
url patterns = [
    url(r'^$', views.index)
]
