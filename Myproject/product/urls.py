from django.urls import path
from . import views 

urlpatterns = [
    path('product/',views.get_all_product,name='products'),
]

