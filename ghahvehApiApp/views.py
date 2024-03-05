from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Product,Category
from .serializers import CategorySerializer,ProductSerializer

@api_view(['GET'])
def index(request):
    return Response({"Success": "The setup was successful"})

@api_view(['GET'])
def GetAllCategories(request):
    get_categories = Category.objects.all()
    serializer = CategorySerializer(get_categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetAllProducts(request):
    get_products = Product.objects.all()
    serializer = ProductSerializer(get_products, many=True)
    return Response(serializer.data)
class ProductListByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)
@api_view(['PUT'])
def UpdateProduct(request):
    post_id = request.data.get('post_id')
    get_new_title = request.data.get('new_title')
    get_new_content = request.data.get('new_content')
    get_image = request.data.get('image')  # Get the image data from request

    try:
        post = Product.objects.get(id=post_id)

        if get_new_title:
            post.title = get_new_title
        if get_new_content:
            post.content = get_new_content
        if get_image:
            post.image = get_image

        post.save()
        return Response({"Success": "The post was successfully updated"}, status=200)

    except Product.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=404)