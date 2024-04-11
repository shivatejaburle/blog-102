from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post

# Show all the list of Posts
class PostList(ListView):
    http_method_names = ['get']
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'
