from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('product_<int:product_id>/', views.product_view, name='product'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
