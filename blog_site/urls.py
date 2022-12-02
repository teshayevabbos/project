from django.urls import path
from django.http import HttpResponse
from .views import BlogListView, BlogDetailView
from .views import  create
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('post/new/', create, name='post_new'),


]