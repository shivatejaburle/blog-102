from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import Post
from django.urls import reverse_lazy
from django.contrib import messages

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

    # To get the required post
    def get_object(self):
        queryset = get_object_or_404(self.model, id=self.kwargs['pk'])
        return queryset

# To Create a new Post
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content']
    http_method_names = ['get', 'post']
    context_object_name = 'form'
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

# To Update the Post
class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content']
    http_method_names = ['get', 'post']
    context_object_name = 'form'
    pk_url_kwarg = 'pk'
    template_name = 'blog/post_form.html'
    # success_url = reverse_lazy('blog:post_list')

    #  Custom Query
    def get_queryset(self):
        queryset = self.model.objects.filter(id=self.kwargs['pk'])
        return queryset
    
    # Add your context data
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PostUpdate, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['form_type'] = 'Update'
        return context
    
    # Customize Success URL
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk' : self.kwargs['pk']})