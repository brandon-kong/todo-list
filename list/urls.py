from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create',),
    path('view/<int:id>', views.view, name="view"),
    path('user/<int:id>', views.getListFromUser, name="user"),
]