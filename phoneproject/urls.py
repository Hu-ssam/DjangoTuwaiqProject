"""
URL configuration for phoneproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from mobile import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.LandPage, name='landpage'),
    path('admin/', admin.site.urls),
    path('welcome/', views.welcome),
    path('getdata/', views.GetData),
    path('datasend/<str:name>', views.datasend),
    path('add/<int:num1>/<int:num2>', views.add),
    path('index/', views.runindex),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('blog/', views.blog, name='blog'),
    path('getphone/', views.getPhoneMenue, name='getphone'),
    path('invoice/', views.invoice,name='invoice'),
    path('details/', views.details, name='details'),
    path('add_to_cart/', views.add_to_cart,name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('auth_login/', views.auth_login, name='login'),
    path('auth_register/', views.auth_register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

