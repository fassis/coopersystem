from django.urls import path
from . import views, api_views

urlpatterns = [

	### API VIEWS ###
    path('', api_views.index, name="list"),
	path('urls', api_views.api_overview, 
		name="api-overview"),
	path('product-list/', 
		api_views.api_product_list, 
		name="product-list"),
	path('product-detail/<str:pk>/', 
		api_views.api_product_detail, 
		name="product-detail"),
	path('product-create/', 
		api_views.api_product_create, 
		name="product-create"),

	path('product-update/<str:pk>/', 
		api_views.api_product_update, 
		name="product-update"),
	path('product-delete/<str:pk>/', 
		api_views.api_product_delete, 
		name="product-delete"),

	### VIEWS ###

	path('product_list', 
        views.product_list, 
		name='product_list'),
	
	path('order_list', 
        views.order_list, 
        name='order_list'),
]