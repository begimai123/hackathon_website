from django.urls import path
from . import views
from .views import *

app_name='shop'

urlpatterns=[
    path('',views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'),

]
