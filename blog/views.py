from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView, DeleteView
from .models import Post
from django.views.generic import TemplateView
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.

posts = [
    {
        'author': 'Mike',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '6 November, 2019'
    }
]


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        Pr = Profile.user.username
        user = get_object_or_404(Profile, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.author:
            return True
        return False


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', posts)
