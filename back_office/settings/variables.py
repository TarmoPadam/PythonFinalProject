from . import models


def variable(request):
    variable = models.Variables.objects.first()
    return {'variable': variable}
