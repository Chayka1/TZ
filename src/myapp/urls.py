from django.urls import path

from myapp.api import item_list

urlpatterns = [
    path("items/", item_list, name="item_list"),
]
