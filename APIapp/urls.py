# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Users
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    # Products
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),

    # Tasks
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
]