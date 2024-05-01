from django.shortcuts import render
from django.views.generic import DetailView
from profiles.models import Profile
from django.contrib.auth.models import User

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