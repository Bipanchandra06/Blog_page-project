from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,time
from ckeditor.fields import RichTextField
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
    def get_absolute_url(self):
        return reverse('home')

class profile(models.Model):
    bloguser=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio= models.TextField(blank=True,null=True)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='images/profile/')
    websitelink=models.CharField(null=True,blank=True,max_length=255)
    instagramlink=models.CharField(null=True,blank=True,max_length=255)
    def __str__(self):
        return str(self.bloguser)

class post(models.Model):
    title = models.CharField(max_length=255)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    header_image=models.ImageField(null=True,blank=True,upload_to='images/')
    body= RichTextField(blank=True,null=True)
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255,default='coding')
    snippet=models.CharField(max_length=255)
    likes=models.ManyToManyField(User,related_name='blog_posts')
    def totallikes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.title)+' | '+str(self.author)
    def get_absolute_url(self):
        return reverse('home')
    