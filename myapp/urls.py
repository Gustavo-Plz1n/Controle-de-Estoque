"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from .views import *
from . import views
import emp.views as fun
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",login_view),
    path("about/",about),
    path("services/",services),
    path('login/', login_view),
    path("emp/",include('emp.urls')),
    path('logout/', login_view),
    path('bemvindo/', views.bemvindo, name='bemvindo')
]
#user = admin
#pass = toor@123