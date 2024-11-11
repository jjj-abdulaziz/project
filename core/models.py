from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.conf import settings

STATUS_CHOICE = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered")
)
STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published")
)
RATING = (
    (1, "★"),
    (2, "★★"),
    (3, "★★★"),
    (4, "★★★★"),
    (5, "★★★★★")
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100, default="leather") 
    image = models.ImageField(upload_to="category", default="category.jpg")
    
    class Meta:
        verbose_name_plural = "categories"
    
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title

# class Tag(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefgh12345")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, default="Handbag") 
    image = models.ImageField(upload_to="product", default="product.jpg")
    description = models.TextField(null=True, blank=True, default="This is the product")
    options = models.JSONField(default=dict)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    specifications = models.TextField(null=True, blank=True)
    # tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890")
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "products"
    
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title

class ProductImage(models.Model):
    images = models.ImageField(upload_to="product_images", default="product.jpg")
    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)    
    
    class Meta:
        verbose_name_plural = "product Images"

#################################cart, order, orderitems ###################################

class CartOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="process")    
    
    class Meta:
        verbose_name_plural = "Cart Orders"

class CartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    items = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    
    class Meta:
        verbose_name_plural = "Cart Order Items"

def order_img(self):
    return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))        

#################################product review, wishlist, address ###################################   

class ProductReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=1)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Reviews"
    
    def __str__(self):
        return self.product.title 
    
    def get_rating(self):
        return self.rating

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Wishlists"
    
    def __str__(self):
        return self.product.title 

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Addresses"
