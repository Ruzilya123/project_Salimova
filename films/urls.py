
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("add/", views.add),
    path("edit/<int:pk>/", views.edit),
    path("delete/<int:pk>/", views.delete),
]
