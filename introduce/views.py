from django.shortcuts import render
from .models import AccessLog

# Create your views here.
def introduce(request):
    new_access = AccessLog()
    new_access.location = request.path+'introduce.html'
    new_access.save()

    return render(request, 'introduce.html')