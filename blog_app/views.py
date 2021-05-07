from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from blog_app.models import Post


class BlogAppView(ListView):
    model = Post
    template_name = 'home.html'
    # context_object_name = 'posts_in_blog'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'
