from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.serializers import ProductSerializer

from core.models import Product
# Create your views here.

def index(request):
	return render(request, 'base.html')

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