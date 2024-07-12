from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {"favicon":"logos/favicon.ico"}
    return render(request, "chat/index.html", context)