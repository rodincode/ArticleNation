
from django.urls import path
from .views import *

from django.contrib.auth import views as auth

# . means same directory
# .views

urlpatterns = [
    path('', homepage, name = 'home'),
    path('article', articlepage, name = 'article'),
    path('about', about_me, name = 'about'),
    path('post', post_article, name = 'post'),
    path('thankyou', thankyou, name = 'thankyou'),
    path('allposts', allposts, name = 'allposts'),
    path('likes', homepagewithlikes, name= "likes"),
    path('login/', Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='ArticleNation/logout.html'), name ='logout'),
    path('register/', register, name ='register'),
    path('search/', SearchView.as_view(template_name ='ArticleNation/search.html'), name ='search')
    
]

# first is what is give in url
# 2 is view name
# 3 how django will call it/ knows it