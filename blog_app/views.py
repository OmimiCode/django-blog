from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog_app.models import Post


class BlogAppView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts_in_blog'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'


class NewPost(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'


class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
