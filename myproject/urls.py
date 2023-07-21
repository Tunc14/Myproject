"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path 
from myapp.views import (
    customer_list,
    search_customer,
    edit_customer,
    delete_customer,
    register_customer,
)
urlpatterns = [
    path('', customer_list,name='customer_list'),
    path('search/',search_customer,name='search_customer'),
    path('edit/<int:customer_id>/',edit_customer,name='edit_customer'),
    path('delete/<int:customer_id>/',delete_customer, name='delete_customer'),
    path('register/',register_customer,name='register_customer'),
]
