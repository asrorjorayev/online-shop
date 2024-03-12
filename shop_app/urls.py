from django.urls import path
from .import views
from .views import *



urlpatterns=[
    # path('',index,name='index'),
    path('login_page/',login_page,name='login_page'),
    path('logout_page/',logout_page,name='logout_page'),
    path('register/', Register_page,name='register'),
    path('profile/',views.ProfileViev.as_view(),name='profile_page')

]