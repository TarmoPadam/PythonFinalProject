from django.shortcuts import render, redirect
from .models import Variables


def settings(request):
    variables = Variables.objects.first()

    if request.method == 'POST':
        website_title = request.POST.get("title")
        description = request.POST.get("description")
        currency = request.POST.get("currency")
        if website_title:
            variables.website_title = website_title
        if description:
            variables.homepage_description = description
        if currency:
            variables.website_currency = currency
    variables.save()
    return render(request, "settings.html", {'variables': variables})
