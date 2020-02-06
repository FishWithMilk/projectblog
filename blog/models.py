from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount


class Post(models.Model, HitCountMixin):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='post_pics')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', help_text="Select a category for this article", blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=20, help_text="Enter article category")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    @property
    def count(self):
        return Post.objects.filter(category=self).count()


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
