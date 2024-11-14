from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.greet_user, name="greet_user"),
    path("calculate-age/", views.calculate_age, name="calculate_age"),
    path("order-summary/", views.order_summary, name="order_summary"),
    path("admin/", admin.site.urls),
]

