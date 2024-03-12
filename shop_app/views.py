from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render,reverse,get_list_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm,ProfileForm
from django.http import HttpResponseRedirect,HttpResponse
from .models import User
from django.views.generic import UpdateView
from django.urls import reverse_lazy

# def index(request):
#     return render(request,'index.html')


def login_page(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))
    form=LoginForm()
    data={
        'form':form
    }
    return render(request,'login_page.html',context=data)


def logout_page(request):
     logout(request)
     return HttpResponseRedirect(reverse('login_page'))


def Register_page(request):
    if request.method=="POST":
          form=RegisterForm(request.POST)
          if form.is_valid():
                try:
                    user=User()
                    user.first_name=form.cleaned_data['first_name']
                    user.last_name=form.cleaned_data['last_name']
                    user.username=form.cleaned_data['username']
                    user.set_password(form.cleaned_data['password'])
                    user.save()
                    return HttpResponseRedirect(reverse('login_page'))
                except Exception as e:
                    print(e)
                    return HttpResponseRedirect(reverse('register'))
    form=RegisterForm()
    data={
         'form':form
    }
    return render(request,'register.html',context=data)

class ProfileViev(UpdateView):
    form_class=ProfileForm
    model=User
    template_name='profile.html'

    def get_object(self, queryset=None):
          return self.request.user
    def get_success_url(self):
         return reverse_lazy('profile_page')

