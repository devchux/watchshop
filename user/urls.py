from django.urls import path
from .views import register_user, login_user, logout_user, profile, cart, remove_cart, add_to_cart

urlpatterns = [
    path('register/', register_user, name="user-register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('profile/', profile, name="profile"),
    path('cart/', cart, name='cart'),
    path('orders/remove/<int:id>/', remove_cart, name='remove_cart'),
    path('orders/add/<int:id>/', add_to_cart, name='add_to_cart'),
]
