from django.conf.urls import url

from . import views

app_name = 'books'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='book_list'),
    url(r'^books/create/$', views.book_create, name='book_create'),
    url(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    url(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
]
