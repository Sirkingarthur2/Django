from django.shortcuts import render
from app.forms import AgeCalculationForm, UserGreetingForm, OrderForm

def greet_user(request):
    form = UserGreetingForm(request.GET or None)
    name = None
    if form.is_valid():
        name = form.cleaned_data["name_data"]
    return render(request, "greet_user.html", {"form": form, "name": name})

def calculate_age(request):
    form = AgeCalculationForm(request.GET or None)
    age = None
    if form.is_valid():
        end_year = form.cleaned_data["end_year"]
        birth_year = form.cleaned_data["birth_year"]
        age = end_year - birth_year
    return render(request, "calculate_age.html", {"form": form, "age": age})

def order_summary(request):
    form = OrderForm(request.GET or None)
    total = None
    if form.is_valid():
        burgers = form.cleaned_data["burgers"]
        fries = form.cleaned_data["fries"]
        drinks = form.cleaned_data["drinks"]
        total = f"{burgers * 4.5 + fries * 1.5 + drinks * 1:.2f}"
    return render(request, "order_summary.html", {"form": form, "total": total})