"""mypythbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from bank import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login/', views.signin, name="login"),
    path('signup/', views.signup, name="signup"),
    path('main/', views.main, name="main"),
    path('transfer/', views.transfer, name="transfer"),
    path('logout/', views.signout, name="logout"),
    path('references/<int:id>', views.references, name="references"),
    path('history/', views.history, name="history")
]

handler404 = "bank.views.error404"