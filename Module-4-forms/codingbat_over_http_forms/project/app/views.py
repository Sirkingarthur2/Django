from django.shortcuts import render
from app.forms import *

def font_times(request):
    form = FontTimes(request.GET)
    
    if form.is_valid():
        user_string = form.cleaned_data["string_input"]
        user_integer = form.cleaned_data["integer_input"]

        final_string = user_string[0:3] * user_integer

        return render(request, "font_times.html", { "form": form, "final_string": final_string})
    else:
        return render(request, "font_times.html", {"form": form})

def no_teen_sum(request):
    form = NoTeenSum(request.GET)
    if form.is_valid():
        user_int_1 = form.cleaned_data["integer_1"]
        user_int_2 = form.cleaned_data["integer_2"]
        user_int_3 = form.cleaned_data["integer_3"]
        final_sum = 0

        if user_int_1 in range(13, 20):
            user_int_1 = 0
            
        if user_int_2 in range(13, 20):
            user_int_2 = 0

        if user_int_3 in range(13, 20):
            user_int_3 = 0

        final_sum = user_int_1 + user_int_2 + user_int_3
        return render(request, "no_teen_sum.html", {'form': form, 'final_sum': final_sum})
    else:
        return render(request, "no_teen_sum.html", {"form": form})

def xyz_there(request):
    form = XyzThere(request.GET)
    if form.is_valid():
        user_given = form.cleaned_data["given_string"]
        # Check if 'xyz' is present not preceded by a dot
        user_given_result = ('xyz' in user_given) and (user_given.find('.xyz') == -1)
        return render(request, "xyz_there.html", {"form": form, "user_given": user_given_result})
    else:
        return render(request, "xyz_there.html", {"form": form})

def centered_average(request):
    form = CenteredAverage(request.GET)

    if form.is_valid():
        user_list = [
            form.cleaned_data["given_amount_1"],
            form.cleaned_data["given_amount_2"],
            form.cleaned_data["given_amount_3"],
            form.cleaned_data["given_amount_4"],
            form.cleaned_data["given_amount_5"],
        ]

        given_amount_6 = form.cleaned_data["given_amount_6"]
        given_amount_7 = form.cleaned_data["given_amount_7"]

        if given_amount_6:
            user_list.append(given_amount_6)
        if given_amount_7:
            user_list.append(given_amount_7)

        if len(user_list) > 2:
            user_list.sort()
            user_list = user_list[1:-1]  
            centered_avg = sum(user_list) / len(user_list) 
            centered_avg = int(centered_avg)
        else:
            centered_avg = None

        return render(request, "centered_average.html", {
            "form": form,
            "centered_avg": centered_avg
        })
    else:
        return render(request, "centered_average.html", {"form": form})