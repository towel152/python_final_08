"""
URL configuration for python_final_08 project.

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
from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('', views.index),      # 設定執行首頁顯示的功能由index函式負責
    path('home/', views.home),
    path('about/', views.about),
    path('news/', views.news),
    path('data/', views.data),
    path('quantity/', views.quantity, name='quantity'),
    path('crimerate/', views.crime_rates, name='crimerate'),
    path('compare/', views.compare, name='compare'),
    path('dbtest/', views.people),
    path('admin/', admin.site.urls),
]
