from django.shortcuts import render, redirect
from .forms import VariablesForm
from .models import Variables


def settings(request):
    variables = Variables.objects.first()

    if request.method == 'POST':
        form = VariablesForm(request.POST, instance=variables)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = VariablesForm(instance=variables)

    return render(request, "settings.html", {'form': form})
