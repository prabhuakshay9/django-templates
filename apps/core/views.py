from django.shortcuts import render


def index(request):
    """ Dashboard View """
    return render(request, template_name="core/index.html")
