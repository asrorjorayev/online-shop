from django.db import models
from django.contrib.auth.models import  AbstractUser

Mijoz,Xodim,Admin=('mijoz','xodim','admin')
user_roles=((Mijoz,Mijoz),(Xodim,Xodim),(Admin,Admin))

class BaseModel(models.Model):
    created_ad=models.DateTimeField(auto_now_add=True)
    updated_ad=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class User(AbstractUser,BaseModel):
    phone=models.CharField(max_length=13,unique=True,null=True,blank=True)
    bio=models.CharField(max_length=100,null=True,blank=True)
    user_roles=models.CharField(max_length=40,choices=user_roles)
    image=models.ImageField(upload_to='image',)

    def __str__(self):
        return self.username
