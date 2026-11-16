from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem

def home(request):
    productos_reales = Product.objects.all()
    return render(request, 'index.html', {'products': productos_reales})

@login_required(login_url='/admin/login/')
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)
    carrito, creado = Cart.objects.get_or_create(user=request.user)
    item, item_creado = CartItem.objects.get_or_create(cart=carrito, product=producto)
    
    if not item_creado:
        item.quantity += 1
        item.save()
        
    return redirect('home')

@login_required(login_url='/admin/login/')
def ver_carrito(request):
    carrito, creado = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=carrito)
    
    return render(request, 'carrito.html', {'items': items, 'carrito': carrito})