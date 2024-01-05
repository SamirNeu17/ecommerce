from django.urls import path
import products.views as product_views


urlpatterns = [
    path("detail/<int:product_id>", product_views.product_detail, name="product_detail"),
    path("carts", product_views.shopping_cart, name="shopping_cart"),
    path("add-to-cart/<int:product_id>", product_views.add_to_cart, name="add_to_cart"),
    path("remove-cart/<int:cart_id>", product_views.remove_cart_item, name="remove_cart_item"),
]