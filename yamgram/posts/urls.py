from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.postCreate, name='postCreate'),
    path('like/<int:post_id>/', views.like, name='like'),
    path('dislike/<int:post_id>/', views.dislike, name='dislike'),
]