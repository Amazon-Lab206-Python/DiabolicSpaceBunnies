
from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^random_word$', views.index),
    url(r'^random_word/reset$', views.reset),
]
