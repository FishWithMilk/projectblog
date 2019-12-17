from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from blog.models import Post, Category


def social(request):
    category = get_object_or_404(Category, name=Post.category.name)
    count = Post.objects.filter(category=category).count()

    context = {
        'count': count,
    }

    return context
