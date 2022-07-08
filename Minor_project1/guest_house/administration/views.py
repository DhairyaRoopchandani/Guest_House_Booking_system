from django.shortcuts import render
from django.http import HttpResponse
def administration(request):
    return HttpResponse("This is administration section")
