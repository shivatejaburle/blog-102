from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from profiles.models import Profile
from django.contrib.auth.models import User
import os

# User Profile Detail View
class UserProfile(DetailView):
    model = Profile
    # context_object_name = 'profile'
    # template_name = 'profiles/profile_detail.html'
    
    # def get_queryset(self):
    #     userId = User.objects.filter(id = self.kwargs['pk'])
    #     print(userId[0].profiles.id)
    #     queryset = self.model.objects.filter(id = userId[0].profiles.id)
    #     return queryset

# Update User Profile
class UpdateUserProfile(UpdateView):
    model = Profile
    fields = ['first_name','last_name', 'mobile', 'address']

    def get_success_url(self):
        return reverse_lazy('profiles:profile_detail', kwargs={'pk' : self.kwargs['pk']})

# Update Profile Picture
def UpdateProfilePicture(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if profile.image:
                os.remove(profile.image.path)
            profile.image = request.FILES['image_document']
        profile.save()
        success_url = '/profile/detail/' + str(profile.id)
        return redirect(success_url)
    context = {'profile':profile}
    return render(request, 'profiles/picture_form.html', context)

# Remove Profile Picture
def DeleteProfilePicture(request, pk):
    profile = Profile.objects.get(id=pk)
    os.remove(profile.image.path)
    profile.image=""
    profile.save()
    success_url = '/profile/detail/' + str(profile.id)
    return redirect(success_url)
