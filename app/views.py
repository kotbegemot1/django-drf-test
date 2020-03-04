from django.shortcuts import render
from app.models import Post  
from app.serializers import PostSerializer  
from rest_framework import generics  
# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
        

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
