from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
  
# Create your views here.

# types of request
# request = get me to page (default)
# request = let me post
# Need only these two

# (GET
# POST
# PUT
# HEAD
# DELETE
# PATCH
# OPTIONS
# )

# etc.

  
  
########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('ArticleNation/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            #msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'ArticleNation/register.html', {'form': form, 'title':'reqister here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'ArticleNation/login.html', {'form':form, 'title':'log in'})





def homepage(request):
    Data = Article.objects.order_by('title')
    return render(request, 'ArticleNation/home.html',
    {'Data':Data,
    "Post1": Data[0],
    "Post2": Data[1],
    "Post3": Data[2]})

def homepagewithlikes(request):
    Data = get_object_or_404(Article,id=request.POST.get('likesbutton'))
    if request.user.is_authenticated:
        Data.likes.add(request.user)
    return HttpResponseRedirect(reverse('home'))
        
def articlepage(request):
    return render(request, 'ArticleNation/index.html')

def about_me(request):
    return render(request, 'ArticleNation/About me.html')

def post_article(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(request.POST)
        if form.is_valid():
            post = form.save()
            print(post)
            post.save()
            return redirect("thankyou")

    else:
        form = PostForm()

    return render(request, 'ArticleNation/Post article.html', {'form': form})

def thankyou(request):
    return render(request, 'ArticleNation/Thankyou.html')

def allposts(request):
    Data = Article.objects.order_by('title')
    #print(Data)
    return render(request, 'ArticleNation/allposts.html',{"Data":Data})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            Data = get_object_or_404(Article,id=request.POST.get('likesbutton'))
            Data.likes.add(request.user)
        return HttpResponseRedirect(reverse('article_detail',kwargs={'pk': pk}))
    return render(request, 'ArticleNation/article_detail.html', {'article': article})

class SearchView(ListView):
    model = Article
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Article.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result