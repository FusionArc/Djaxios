from django.contrib import admin
from django.urls import path
from apps.cart.views import cart_detail
from apps.core.views import frontpage, contact, about
from apps.store.views import product_detail, category_detail

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('cart/', cart_detail, name='cart'),
    path('contact/', contact, name='contact'),
    path('<slug:slug>/', category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
]
