from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path("detail/<int:pk>", views.UserProfile.as_view(), name = 'profile_detail'),
    path("update/<int:pk>", views.UpdateUserProfile.as_view(), name = 'profile_update'),
    # Update Profile Picture
    path("update/picture/<int:pk>", views.UpdateProfilePicture, name = 'picture_update'),
    # Delete Profile Picture
    path("delete/picture/<int:pk>", views.DeleteProfilePicture, name = 'picture_delete')
]