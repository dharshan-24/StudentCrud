from django.urls import path
from .import views

urlpatterns = [
    path("add/",views.add_student),
    path("all/",views.get_student),
    path("update/<int:id>/",views.update_student),
    path("delete/<int:id>/",views.delete_student),
]
