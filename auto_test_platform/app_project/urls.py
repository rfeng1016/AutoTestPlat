from django.urls import path
from app_project import views

urlpatterns = [

    # 项目管理
    path('', views.project_manage),
    path('add_project/', views.add_project),
    path('delete_project/<int:pid>/', views.delete_project),
    path('edit_project/<int:pid>/', views.edit_project),


    # 接口

]