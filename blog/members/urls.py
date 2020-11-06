from django.urls import path
from .views import UserSignUpView, UserEditView

urlpatterns = [
    path('register/', UserSignUpView.as_view(), name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile')
]