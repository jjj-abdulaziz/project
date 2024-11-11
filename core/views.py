from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.template.loader import render_to_string

from core.models import Product, Category, CartOrder, CartOrderItem, ProductImage, ProductReview, Wishlist, Address


# Create your views here.
def index(request):
    products = Product.objects.filter(product_status="published", featured=True)
    context = {
        "products":products
    }
    return render(request, 'core/index.html', context)



def shop(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    
    return render(request, 'core/shop.html', context)

def blog(request):
    return render(request, 'core/blog.html')

def blog1(request):
    return render(request, 'core/blog1.html')

def blog2(request):
    return render(request, 'core/blog2.html')

def blog3(request):
    return render(request, 'core/blog3.html')

def blog4(request):
    return render(request, 'core/blog4.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def cart(request):
    return render(request, 'core/cart.html')

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    # product = get_object_or_404(Product, pid=pid)
    product_image = product.product_images.all()
    
    context = {
        "product": product,
        "product_image":product_image,
    }
    return render(request, "core/product-detail.html", context)

def add_to_cart(request):
    cart_product = {}
    
    cart_product[str(request.GET['id'])] = {
        
        'title': request.GET['title'],  
        'quantity': request.GET['quantity'],
        'Type': request.GET['type'],
        'price': request.GET['price']
    }
    
    if 'cart_data_object' in request.session:
        if str(request.GET['id']) in request.session['cart_data_object']:
            
            cart_data = request.session['cart_data_object']
            cart_data[str(request.GET['id'])]['quantity'] = int(cart_product[str(request.GET['id'])]['quantity'])
            cart_data.update(cart_data)
            request.session['cart_data_object'] = cart_data
        else:
            cart_data = request.session['cart_data_object'] 
            cart_data.update(cart_product)
            request.session['cart_data_object'] = cart_data
    else:
        request.session['cart_data_object'] = cart_product
    return JsonResponse({"data": request.session['cart_data_object'], 'totalcartitems': len(request.session['cart_data_object'])})


def cart(request):
    cart_total_amount = 0  
    if "cart_data_object" in request.session:
        for product_id, item in request.session['cart_data_object'].items():
            cart_total_amount += int(item['quantity']) * float(item['price'])
        return render(request, "core/cart.html", {"cart_data": request.session['cart_data_object'], 'totalcartitems': len(request.session['cart_data_object']),  'cart_total_amount':cart_total_amount})
    else:
        messages.warning(request, "Your cart is empty")
        return redirect("core:index")
def delete_item_from_cart(request):
    product_id = str(request.GET.get('id', ''))
    
    if "cart_data_object" in request.session:
        cart_data = request.session.get('cart_data_object', {})
        
        if product_id in cart_data:
            del cart_data[product_id]
            request.session['cart_data_object'] = cart_data
            
    cart_total_amount = 0  
    if "cart_data_object" in request.session:
        cart_data = request.session['cart_data_object']
        for item in cart_data.values():
            cart_total_amount += int(item['quantity']) * float(item['price'])    
            
    context = {
        "cart_data": request.session.get('cart_data_object', {}),
        'totalcartitems': len(request.session.get('cart_data_object', {})),
        'cart_total_amount': cart_total_amount
    }
    context_html = render_to_string("core/cart.html", context)
    
    response_data = {
        "data": context_html,
        'totalcartitems': len(request.session.get('cart_data_object', {}))
    }
    
    return JsonResponse(response_data)