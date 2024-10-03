"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp import views  # Import views from the 'myapp' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'), # Hello route
    path('users/', views.users, name='users'),  #users route
    path('new_user/', views.new_user, name='new_user'), # new_user
    path('users/<int:id>/', views.user_detail, name='user_detail'),

]