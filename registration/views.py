from django.shortcuts import render
from .form import Customerform
from django.http import HttpResponse


def index(request):
    form = Customerform()
    if request == 'POST':
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render(request, 'HSA/index.html', context)
