from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from .views import PostListView,\
    PostDetailView,\
    PostCreateView,\
    PostUpdateView,\
    PostDeleteView,\
    UserPostListView

urlpatterns = [
    path('index/', PostListView.as_view(), name='index_url'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', TemplateView.as_view(template_name='blog/about.html'), name='about_url'),
    path('contact/', TemplateView.as_view(template_name='blog/contact.html'), name='contact_url'),
    path('post/', TemplateView.as_view(template_name='blog/post.html'), name='post_url'),
]
