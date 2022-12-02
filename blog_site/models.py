from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(post):
        return post.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    img = models.ImageField(upload_to='image/post_img/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(post):
        return post.title
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])