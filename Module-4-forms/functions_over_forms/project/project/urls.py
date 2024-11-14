from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("", greet_user, name="greet_user"),
    path("age-in/", age_in, name="age-in"),
    path("order-total/", order_total, name="order_total"),
    path("admin/", admin.site.urls),
]