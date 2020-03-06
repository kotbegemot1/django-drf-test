from django.db import models  
from django.utils import timezone  
from django.contrib.auth.models import User


class Post(models.Model):  
    title = models.CharField(max_length=255)  
    slug = models.SlugField  
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])  
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)  
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete = models.SET_NULL, related_name='posts')
    author = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
