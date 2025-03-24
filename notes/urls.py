from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create-item/',views.create_item,name="create-item"),
    path('upadate-item/<str:pk>/',views.update_item,name="update-item"),
    path('delete-item/<str:pk>/',views.delete_item,name="delete-item")
]
