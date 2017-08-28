from django.conf.urls import url

from . import views

app_name = 'books'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='book_list'),
    url(r'^books/create/$', views.book_create, name='book_create'),
]
