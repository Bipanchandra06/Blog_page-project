from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import profile

class signup(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
    name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':"form-control"}))
    class Meta:
        model=User
        fields=('email','name','username','password1','password2')
    def __init__(self,*args,**kwargs):
        super(signup,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'

class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
        }

class updatepass(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'type':'password'}))
    new_password1=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':"form-control",'type':'password'}))
    new_password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':"form-control",'type':'password'}))
    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')

class profilepageform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['bio','profile_pic','websitelink','instagramlink']
        widgets={
                "bio": forms.Textarea(attrs={"class": "form-control"}),
                #"profile_pic": forms.ImageField(attrs={"class": "form-control"}),
                "websitelink": forms.TextInput(attrs={"class": "form-control"}),
                "instagramlink": forms.TextInput(attrs={"class": "form-control"}),}

class profileditform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['bio','profile_pic','websitelink','instagramlink']
        widgets={
                "bio": forms.Textarea(attrs={"class": "form-control"}),
                #"profile_pic": forms.ImageField(attrs={"class": "form-control"}),
                "websitelink": forms.TextInput(attrs={"class": "form-control"}),
                "instagramlink": forms.TextInput(attrs={"class": "form-control"}),}