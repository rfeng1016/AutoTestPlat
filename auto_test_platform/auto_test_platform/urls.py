"""auto_test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include

from app_users import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 用户管理
    path('index/', views.index),
    path('accounts/login/', views.index),
    path('logout/', views.logout),

    # 项目管理
    path('project/', include('app_project.urls')),

    # 模块管理
    path('module/', include('app_module.urls')),

    # 用例管理

    # 任务管理
]
