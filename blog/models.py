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
    likes = models.ManyToManyField('users.CustomUser', related_name='likes', blank=True)
    category = models.ManyToManyField('Category', help_text="Select a category for this article", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_like_url(self):
        return reverse('like-toogle', kwargs={'pk': self.pk})

    def get_api_like_url(self):
        return reverse('like-api-toogle', kwargs={'pk': self.pk})

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, help_text="Enter article category")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
