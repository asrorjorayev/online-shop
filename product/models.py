from django.db import models
from shop_app.models import User,BaseModel


class Category_product(BaseModel):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Categoriya'
        verbose_name_plural='Categoriyalar'


class Product(BaseModel):
    name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='products')
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category_product,on_delete=models.CASCADE,related_name='products')
    about=models.TextField(default='',null=True,blank=True)
    image=models.ImageField(upload_to='pr_image/',null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Mahsulot'
        verbose_name_plural='Mahsulotlar'



# Create your models here.
