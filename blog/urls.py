# blog/urls.py
from django.urls import path
from .views import post_list, post_detail, post_archive

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('archive/<int:year>/<int:month>/', post_archive, name='post_archive'),
]
