from django.urls import path
from . import views

urlpatterns = [
    path("function/", views.hello, name="hello"),
    path("class/", views.HaloView.as_view(), name="haloview"),
    path("reservation/", views.home, name="reservation_home"),
    path("reservation/<int:pk>/cancel/", views.reservation_cancel, name="reservation_cancel"),
]
