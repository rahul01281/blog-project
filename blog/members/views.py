from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from blog_app.models import UserProfile

# Create your views here.

class UserSignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        #users = UserProfile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id = self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'facebook_url', 'instagram_url', 'twitter_url']
    success_url = reverse_lazy('home')

class CreateProfilePageView(generic.CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html'

    # making user id available to profile so that when we save the form it gets saved under the right user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
