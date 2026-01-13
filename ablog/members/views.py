from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import signup,EditProfileForm,updatepass,profilepageform,profileditform
from theblog.models import profile,post
# Create your views here.
class profileview(generic.DetailView):
    model=profile
    template_name='registration/userprofile.html'
    def get_context_data(self, *args ,**kwargs):
        
        context = super(profileview, self).get_context_data(*args ,**kwargs)
        page_user=get_object_or_404(profile,id=self.kwargs['pk'])
        userposts=list(post.objects.filter(author=page_user.bloguser))
        context['page_user']= page_user
        context['userposts']=userposts
        return context

class register_form(generic.CreateView):
    form_class=signup
    template_name='registration/registration.html'
    success_url=reverse_lazy("login")
class update_form(generic.UpdateView):
    form_class=EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy("login")
    def get_object(self):
        return self.request.user
class passwordupdate(PasswordChangeView):
    form_class=updatepass
    template_name='registration/change-password.html'
    success_url=reverse_lazy('home')
class profileedit(generic.UpdateView):
    form_class=profileditform
    template_name='registration/userprofileedit.html'
    success_url=reverse_lazy('home')
    def get_object(self):
        prof=profile.objects.get(bloguser=self.request.user)
        return prof
class profilecreate(generic.CreateView):
    form_class=profilepageform
    template_name='registration/userprofilecreate.html'
    success_url=reverse_lazy('home')
    def form_valid(self, form):
        form.instance.bloguser=self.request.user
        return super().form_valid(form)
    