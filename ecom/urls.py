from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('shop/<int:id>/', detail, name='detail'),
    path('about/', about, name='about'),
]