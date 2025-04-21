from django.forms import ModelForm
from django.forms import ImageField, FileInput
from cloudinary.models import CloudinaryField

from blog.models import Post

class PostForm(ModelForm):
    # image = ImageField(widget=FileInput, label="Upload New Image")
    image = CloudinaryField()
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

