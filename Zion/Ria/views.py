from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer, CartSerializer, CartItemSerializer
from rest_framework import status

@api_view(['GET'])
@permission_classes([AllowAny])
def products(request):
    produc = Product.objects.all()
    serializer = ProductSerializer(produc, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([AllowAny])
def product(request, id):
    pro = Product.objects.get(id=id)
    serializer = ProductSerializer(pro, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
    # Admin only function
    user = request.user
    if not user.is_staff:
        return Response({"detail": "Only Admins can add products"})

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_cart(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_items(request, cart_id):
    user = request.user
    try:
        cart = Cart.objects.get(user=user, id=cart_id)
        cart_items = CartItem.objects.filter(cart=cart_id)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)
    except Cart.DoesNotExist:
        return Response({"detail": "No cart available for this user"})


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_cart_item(request, id):
#     current_cart = Cart.objects.get(id=id)
#     data = request.data
#     user = request.user
#     try:
#         cart = Cart.objects.get(user=user)
#     except Cart.DoesNotExist:
#         return Response({"detail": "No cart available for this user"})

#     product_id = data.get('product_id')
#     try:
#         product = Product.objects.get(id=product_id)
#     except Product.DoesNotExist:
#         return Response({"detail": "Invalid product id"})
    
#     quantity = data.get('quantity')
#     if quantity <= 0:
#         return Response({"detail": "Quantity must be greater than 0"})

#     cart_item, created = CartItem.objects.get_or_create(
#         cart=cart, product=product)
#     cart_item.quantity += quantity
#     cart_item.save()

#     return Response({"detail": "Cart item added successfully"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_cart_item(request, cart_id):
    current_cart = get_object_or_404(Cart, id=cart_id, user=request.user)
    new_cartitem = CartItem(cart=current_cart)
    cart_item = CartItemSerializer(new_cartitem, data=request.data)
    cart_item.is_valid(raise_exception=True)
    cart_item.save()
    return Response({"detail": "Cart item added successfully"}, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_cart_item(request, product_id, cart_id):
    # data = request.data
    user = request.user
    try:
        cart = Cart.objects.filter(user=user)
    except Cart.DoesNotExist:
        return Response({"detail": "No cart available for this user"})

    # product_id = data.get('product_id')
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"detail": "Invalid product id"})

    try:
        cart_item = CartItem.objects.filter(cart=cart_id, product=product_id)
        cart_item.delete()
        return Response({"detail": "Cart item removed successfully"})
    except CartItem.DoesNotExist:
        return Response({"detail": "Cart item not found"})
    

