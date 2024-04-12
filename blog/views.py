from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from blog.models import Post

# Show all the list of Posts
class PostList(ListView):
    model = Post
    http_method_names = ['get']
    queryset = Post.objects.all()
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'

# Show Post Details
class PostDetail(DetailView):
    model = Post
    http_method_names = ['get']
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    pk_url_kwarg = 'pk'

    def get_object(self):
        queryset = get_object_or_404(self.model, id=self.kwargs['pk'])
        return queryset

