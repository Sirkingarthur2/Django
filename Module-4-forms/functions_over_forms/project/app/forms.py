from django import forms

class AgeCalculationForm(forms.Form):
    end_year = forms.IntegerField(label="End Year")
    birth_year = forms.IntegerField(label="Birth Year")

class OrderForm(forms.Form):
    burgers = forms.IntegerField(label="Number of Burgers")
    fries = forms.IntegerField(label="Number of Fries")
    drinks = forms.IntegerField(label="Number of Drinks")

class UserGreetingForm(forms.Form):
    name_data = forms.CharField(label="Your Name")