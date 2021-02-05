from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('add_list/', views.addtolist, name="add"),
    path('delete_task/', views.delete_task, name="delete")
]
