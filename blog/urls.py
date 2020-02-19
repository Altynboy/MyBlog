from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog-home'),
    path('about', views.about, name='blog-about'),
    path('test', views.bootstrap_test, name='test')
]
