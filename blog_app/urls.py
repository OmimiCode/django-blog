from django.urls import path

from blog_app.views import BlogAppView, PostDetailView

urlpatterns = [
    path('', BlogAppView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(),
         name='post_details')
]