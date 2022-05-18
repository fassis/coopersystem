from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.serializers import ProductSerializer,\
	UserSerializer, RegisterSerializer

from core.models import Product
# Create your views here.

@api_view(['GET'])
def api_overview(request):
	api_urls = {
		'List':'/product-list/',
		'Detail':'/product-detail/<str:pk>/',
		'Create':'/product-create/',
		'Update':'/product-update/<str:pk>/',
		'Delete':'/product-delete/<str:pk>/',
		}

	return Response(api_urls)

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

@api_view(['GET'])
def api_product_list(request):
	Products = Product.objects.all().order_by('-id')
	serializer = ProductSerializer(Products, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def api_product_detail(request, pk):
	Products = Product.objects.get(id=pk)
	serializer = ProductSerializer(Products, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def api_product_create(request):
	serializer = ProductSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def api_product_update(request, pk):
	Product = Product.objects.get(id=pk)
	serializer = ProductSerializer(instance=Product, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def api_product_delete(request, pk):
	Product = Product.objects.get(id=pk)
	Product.delete()

	return Response('Item deletado com sucesso!')