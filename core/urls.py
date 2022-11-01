from django.urls import path
from core import views
   
urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup', views.signup, name = 'signup'),
    path('signin', views.signin, name = 'signin'),
    path('logout', views.logout, name = 'logout'),
    path('upload', views.upload, name = 'upload'),
    path('search', views.search, name = 'search'),
    path('profile/<str:pk>', views.profile, name = 'profile'),
    path('follow', views.follow, name = 'follow'),
    path('like-post',views.like_post,name = 'like-post'),
    path('settings', views.settings, name = 'settings'),
]