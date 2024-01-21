

from django.urls import path
#from . import views
from .views import Home, Article, AddPostView, UpdatePostView, DeletePostView
urlpatterns = [
   # path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('article/<int:pk>', Article.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),

]
