from django.urls import path
from . import views
from .views import register_form,update_form,passwordupdate,profileview,profileedit,profilecreate
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', register_form.as_view(), name='register'),
    path('update_profile',update_form.as_view(),name='updateuser'),
    path('password/',passwordupdate.as_view(),name='password'),
    path('<int:pk>/profile',profileview.as_view(),name='user_profile'),
    path('<int:pk>/profile/edit',profileedit.as_view(),name='profile_edit'),
    path('<int:pk>/profile/create',profilecreate.as_view(),name='profile_create')
    
]
