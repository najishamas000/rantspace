from django.urls import path

from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('project/<slug:_prName>', views.project_detail, name='desc'),
            path('create/', views.create_project, name='create'),
        ]

