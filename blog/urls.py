from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from .views import PostListView, PostDetailView,\
    PostCreateView, PostUpdateView, PostDeleteView,\
    UserPostListView, CategoryListView, CategorySortedListView,\
    PostCreateViewAPI, PostListViewAPI, PostDetailViewAPI

urlpatterns = [
    path('index/', PostListView.as_view(), name='index_url'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/', TemplateView.as_view(template_name='blog/post.html'), name='post_url'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/<str:name>/', CategorySortedListView.as_view(), name='sorted-category'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('about/', views.about, name='about_url'),
    path('contact/', TemplateView.as_view(template_name='blog/contact.html'), name='contact_url'),

    path('api/post/create/', PostCreateViewAPI.as_view(), name='post-create-api'),
    path('api/post/all/', PostListViewAPI.as_view(), name='post-all-api'),
    path('api/post/detail/<int:pk>/', PostDetailViewAPI.as_view(), name='post-detail-api'),
    path('api/base-auth/', include('rest_framework.urls')),
    path('api/djoser-auth/', include('djoser.urls')),
    path('api/djoser-auth_token/', include('djoser.urls.authtoken')),
]
