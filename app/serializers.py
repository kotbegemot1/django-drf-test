from app.models import Post, Category  
from rest_framework import serializers  
from django.contrib.auth.models import User  

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class PostSerializer(serializers.ModelSerializer):  

    author = AuthorSerializer(read_only=True, required=False)

    class Meta:  
        model = Post  
        fields = ['id','author','title','status','content','updated','publication_date','category']

class CategorySerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'posts']