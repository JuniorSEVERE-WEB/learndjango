from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.months_by_int, name="months_by_int"),
    path("<str:month>/", views.months_by_str, name="months_by_str")
]
