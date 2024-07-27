from django.urls import path


from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('mens/', views.mens, name='mens'),
    path('womens/', views.womens, name='womens'),
    path('kids/', views.kids, name='kids'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name="update_item"),
    path('view/', views.view, name='view')
]