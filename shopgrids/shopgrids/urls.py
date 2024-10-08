"""shopgrids URL Configuration

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
from django.urls import path
from django.urls.conf import include
from django.utils.functional import new_method_proxy
from . import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', include('admin.urls')),
    path('', views.home, name='home'),
    path('useraccount/', include('useraccount.urls')),
    path('adminusermanagement/', include('adminusermanagement.urls')),
    path('categorymanagement/', include('categorymanagement.urls')),
    path('productmanagement/', include('productmanagement.urls')),
    path('product_store/', include('product_store.urls')),
    path('cart/', include('cart.urls')),
    path('order_management/', include('order_management.urls')),
    path('warranty/',include('warranty.urls')),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

