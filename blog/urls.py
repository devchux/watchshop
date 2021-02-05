from django.urls import path
from .views import *

urlpatterns = [
    path('', bloghome, name='blog-home'),
    path('<int:pk>/',blog_detail, name='blog_detail')
]