from django.urls import path
from .views import*
from .import views

app_name='product'

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('category/<int:id>/',category,name='category'),
    path('product_detail/<int:pk>/',views.ProductDteailViev.as_view(),name='product_detail'),

    path('savat/',card_summary,name='card_summary'),
    path('card_add/',card_add,name='card_add'),
    path('card_update/',card_update,name='card_update'),
    path('card_delete/',card_delete,name='card_delete'),

]