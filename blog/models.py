from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='post_pics')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    category = models.ManyToManyField('Category', help_text="Select a category for this article", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, help_text="Enter article category")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})