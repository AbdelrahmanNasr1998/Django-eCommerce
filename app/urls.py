from django.urls import path
from app.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('category/<slug:category>/', ProductsView.as_view(), name='Products'),
    path('category/<slug:category>/product/<int:product>/', ProductDetailsView.as_view(), name='Product_Details'),
    path('login/', LoginView.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('register/', RegisterView.as_view(), name='Register'),
    path('favorite/', FavoriteView.as_view(), name='Favorite'),
    path('add_favorite/<int:product_id>/', AddFavoriteView.as_view(), name='Add_Favorite'),
    path('delete_favorite/<int:favorite_id>/', DeleteFavoriteView.as_view(), name='Delete_Favorite'),
    path('cart/', CartView.as_view(), name='Cart'),
]
