from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm
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
class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    http_method_names = ['get', 'post']
    context_object_name = 'form'
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')
    # success_message = "Your post has been created successfully."

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            context = {
                'form':form
            }
            return render(request, self.template_name, context)
        
        # Add the owner of the record
        obj = form.save(commit = False)
        obj.owner = self.request.user
        obj.save()

        messages.success(request, "Department was successfully created.")
        return redirect(self.success_url)
        
# To Update the Post
class PostUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    # fields = ['title', 'content']
    form_class = PostForm
    http_method_names = ['get', 'post']
    context_object_name = 'form'
    pk_url_kwarg = 'pk'
    template_name = 'blog/post_form.html'
    # success_url = reverse_lazy('blog:post_list')
    # success_message = "Your post has been updated successfully."

    # Update Post with Image
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(self.model, id=self.kwargs['pk'])
        if post.owner == self.request.user:
            if request.FILES:
                post.image.delete() # To delete old image
            form = PostForm(request.POST, request.FILES, instance=post)
            if not form.is_valid():
                context = {
                    'form':form
                }
                return render(request, self.template_name, context)

            form.save()
            messages.success(request, "Your post has been updated successfully.")
        else:
            messages.error(request, "Your are not an author of the post.")
        return redirect(self.get_success_url())

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

# To Delete a Post
class PostDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    http_method_names = ['get', 'post']
    pk_url_kwarg = 'pk'
    context_object_name = 'post'
    template_name = 'blog/post_confirm_delete.html'
    # success_message = "Your post has been deleted successfully."

    def get_queryset(self):
        queryset = self.model.objects.filter(id=self.kwargs['pk'])
        return queryset
    
    # Delete Post with Image
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(self.model, id=self.kwargs['pk'])
        if post.owner == self.request.user:
            post.image.delete() # To delete old image
            post.delete()
            messages.success(request, "Your post has been deleted successfully.")
        else:
            messages.error(request, "Your are not an author of the post.")
        return redirect(self.success_url)