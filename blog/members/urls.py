from django.urls import path
from .views import UserSignUpView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserSignUpView.as_view(), name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name = 'registration/change_password.html')),
    path('password/', PasswordsChangeView.as_view(), name = 'change_password'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name = 'user_profile'),
    path('edit_profile_page/<int:pk>', EditProfilePageView.as_view(), name = 'edit_profile_page'),
]