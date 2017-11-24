
from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books$', views.books),
    url(r'^books/add$', views.add),
    url(r'^books/create$', views.create_book),
    url(r'^books/(?P<book_id>\d+)$', views.book_page),
    url(r'^books/(?P<book_id>\d+)/add_new$', views.add_review_from_book),
    url(r'^review/delete/(?P<review_id>\d+)$', views.delete_review),
    url(r'^users/(?P<user_id>\d+)$', views.user_page),
]
