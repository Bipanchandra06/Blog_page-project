from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from.models import post,Category
from .forms import postform,editform
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
# Create your views here.
#def home(request):
#   return render(request,'home.html',{})
class Homeview(ListView):
    model=post
    template_name='home.html'
    ordering=['-id']

    def get_context_data(self, *args ,**kwargs):
        catmenu=Category.objects.all()
        
        context = super(Homeview, self).get_context_data(*args ,**kwargs)
        context['catmenu']=catmenu
        return context
class articledetailview(DetailView):
    model=post
    template_name='atrcile_detailview.html'
    def get_context_data(self, *args ,**kwargs):
        catmenu=Category.objects.all()
        stuff=post.objects.get(id=self.kwargs['pk'])
        totallikes=stuff.totallikes
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        else:
            liked=False
        context = super(articledetailview, self).get_context_data(*args ,**kwargs)
        context['catmenu']=catmenu
        context['totallikes']=totallikes
        context['lik']=liked
        return context
class addpostview(CreateView):
    model=post
    form_class=postform
    template_name='add_post.html'
    #fields='__all__'
class editpostview(UpdateView):
    model=post
    form_class=editform
    template_name='update_view.html'
class delete_view(DeleteView):
    model=post
    template_name='delete-view.html'
    success_url=reverse_lazy('home')
class addcatview(CreateView):
    model=Category
    #form_class=postform
    template_name='add_cat.html'
    fields='__all__'
def categoryview(request,cats):
    category_posts=post.objects.filter(category=cats.replace('-',' '))
    return render(request,'categories.html',{'cats':cats.replace('-',' '),'category_posts':category_posts})
def categorylistview(request):
    category_list=Category.objects.all()
    return render(request,'category_list.html',{'category_list':category_list})
def likeview(request,pk):
    pos=post.objects.get(id=pk)
    liked=False
    if pos.likes.filter(id=request.user.id).exists():
        pos.likes.remove(request.user)
        liked=False
    else:
        pos.likes.add(request.user)
        liked=True
        
    return HttpResponseRedirect(reverse('blog-article',args=[str(pk)]))
 