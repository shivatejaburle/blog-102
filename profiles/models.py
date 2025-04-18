from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Model for User Profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    mobile = models.CharField(max_length=16, blank=True)
    image = ImageField(upload_to="profiles", blank=True)

    def __str__(self):
        return self.user.username
    
# Signal for Creating a User Profile when we sign up
@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

# Signal for Updating a User Profile when we update User Model
@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profiles.save()