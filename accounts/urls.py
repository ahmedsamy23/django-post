from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/' , views.SignupView.as_view() , name='signup'),
    path('profile/' , views.ProfileView.as_view() , name='profile'),
    path('profile/edit/' , views.ProfileEditView.as_view() , name='profile_edit'),
    path('profile/delete/' , views.DeleteProfileView.as_view() , name='profile_delete'),
    ]