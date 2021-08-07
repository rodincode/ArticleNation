from django import forms
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:

        model = Article
        fields = 'author','title','content'
        widgets = {
            "author":forms.TextInput(attrs={"class":'form-control','placeholder':"Enter author"}),
            "title":forms.TextInput(attrs={"class":'form-control','placeholder':"Enter title"}),
            "content":forms.Textarea(attrs={"class":'form-control col-lg-6','id':"content",'placeholder':'Enter content',
            'style':"height: 300px"})
        } 

 
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']