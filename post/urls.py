from django.urls import path 
from . import views


app_name = 'post'
urlpatterns = [
    path('' , views.PostList.as_view() , name='post'),
    path('post_detail/<str:slug>' , views.PostDetail.as_view() , name='post_detail'),
    path('contact-us/', views.FormView.as_view(), name='contact'),
    path('add_post/', views.PostCreate.as_view(), name='add_post'),
    path('update_post/<str:slug>' , views.PostUpdate.as_view() , name='update_post'),
    path('delete_post/<str:slug>', views.PostDelete.as_view(), name='delete_post'),
] 