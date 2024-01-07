from django.shortcuts import render


def back_office_home(request):
    return render(request, "back_office_home_page.html")
