from django import forms 
from .models import post,Category

choices=Category.objects.all().values_list('name','name')
ch_list=[]
for item in choices:
    ch_list.append(item)
class postform(forms.ModelForm):
    class Meta:
        model=post
        fields=('title','snippet','header_image','author','category','body')
        
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control"}),
            'snippet': forms.TextInput(attrs={'class':"form-control"}),
            'header_image':forms.FileInput(attrs={'class':"form-control"}),
            #'author':forms.Select(attrs={'class':"form-control"}),
            'author': forms.TextInput(attrs={'class':"form-control",'value':'','id':'authorname','type':'hidden'}),
            'category':forms.Select(choices=ch_list ,attrs={'class':"form-control"}),
            'body':forms.Textarea(attrs={'class':"form-control"}),
        }
 
class editform(forms.ModelForm):
    class Meta:
        model=post
        fields=('title','snippet','body')
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control"}),
            'snippet': forms.TextInput(attrs={'class':"form-control"}),
            'body':forms.Textarea(attrs={'class':"form-control"}),
        }