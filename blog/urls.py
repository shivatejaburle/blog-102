from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name = 'post_list'),
    path('detail/<int:pk>', views.PostDetail.as_view(), name = "post_detail"),
    path('create/', views.PostCreate.as_view(), name = "post_create"),
    path('update/<int:pk>', views.PostUpdate.as_view(), name = "post_update"),
    path('delete/<int:pk>', views.PostDelete.as_view(), name = "post_delete"),
    path('my-post-lists', views.MyPostList.as_view(), name = 'my_post_list')
]