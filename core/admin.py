from django.contrib import admin
from core.models import Product, Category, CartOrder, CartOrderItem, ProductImage, ProductReview, Wishlist, Address

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ["user", "title", "product_image", "price", "featured", "product_status", "pid"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category_image"]

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ["user", "price", "paid_status", "order_date", "product_status"]

class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product_status", "image", "qty", "price", "total"]

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "review", "rating"]

class WishlistAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "date"]

class AddressAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "status"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItem, CartOrderItemAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
