from django.urls import path
from .views import UserSignUpView

urlpatterns = [
    path('register/', UserSignUpView.as_view(), name='signup'),
]