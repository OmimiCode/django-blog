from django.urls import path

from blog_app.views import BlogAppView, PostDetailView, NewPost, DeletePost, EditPost

urlpatterns = [
    path('', BlogAppView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('post/new/', NewPost.as_view(), name='new_post'),
    path('post/<int:pk>/edit', EditPost.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name='delete_post'),

]