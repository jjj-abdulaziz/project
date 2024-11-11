from django.urls import path
from core.views import index, shop, product_detail_view, blog, blog1, blog2, blog3, blog4, about, contact,add_to_cart, delete_item_from_cart, cart

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("product/<pid>/", product_detail_view, name="product-detail"),
    
    path("shop/", shop, name="shop"),
    path("blog/", blog, name="blog"),
    path("blog1/", blog1, name="blog1"),
    path("blog2/", blog2, name="blog2"),
    path("blog3/", blog3, name="blog3"),
    path("blog4/", blog4, name="blog4"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("cart/", cart, name="cart"),
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    path('delete-from-cart/', delete_item_from_cart, name='delete_from_cart'),
]
