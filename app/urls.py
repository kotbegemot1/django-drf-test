from app.views import *
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('categories/', CategoriesList.as_view(), name='categories-list'),
    path('categories/<int:pk>/', CategoriesDetail.as_view(), name='categories-detail'),
]