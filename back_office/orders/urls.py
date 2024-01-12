from django.urls import path
from . import views


urlpatterns = [
    path('', views.order_list, name='orders'),
    path('<order_number>/',
         views.order_detail, name='order_detail'),
]
