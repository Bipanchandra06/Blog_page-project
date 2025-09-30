
from django.urls import path
from . import views
from .views import Homeview,articledetailview,addpostview,editpostview,delete_view,addcatview,categoryview,categorylistview,likeview
urlpatterns = [
    #path('',views.home,name='home')
    path('',Homeview.as_view(),name='home'),
    path('artcle/<int:pk>',articledetailview.as_view(),name='blog-article'),
    path('add_post/',addpostview.as_view(),name='addpost'),
    path('artile/edit_post/<int:pk>',editpostview.as_view(),name='editpost'),
    path('article/delete/<int:pk>',delete_view.as_view(),name='deletepost'),
    path('add_cat',addcatview.as_view(),name='add_category'),
    path('category/<str:cats>', categoryview,name='categorys'),
    path('category_list',categorylistview,name='categorylist'),
    path('like/<int:pk>',likeview,name='likepost'),
]