"""coopersystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.contrib.auth import views as auth_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from core.api import viewsets
from core.views import  login_api
from core import urls as core_urls

route = routers.DefaultRouter()

route.register(r'products',viewsets.ProductViewSet, basename="Products")
route.register(r'orders',viewsets.OrderViewSet, basename="Orders")

urlpatterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    path('drf_api/', include(route.urls)),
    path('', include(core_urls)),

    ### Login by api form ###
	path('login/', login_api, 
		name="login_api_view"),
        
    ##Traditional login##
    path('login2/', auth_views.LoginView.as_view(template_name='login.html',
         redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), 
        name='logout'),
]
