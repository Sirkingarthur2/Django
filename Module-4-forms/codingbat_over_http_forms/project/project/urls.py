from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("warmup-2/font-times/", font_times, name="font_times"),
    path("logic-2/no-teen-sum/", no_teen_sum, name="no_teen_sum"),
    path("string-2/xyz-there/", xyz_there, name="xyz_there"),
    path("list-2/centered-average/", centered_average, name="centered_average"),
]
 