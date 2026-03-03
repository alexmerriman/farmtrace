from django.shortcuts import render
from django.http import HttpResponse
from .models import Page

def index(request):
    pg = Page.objects.get(permalink='/')
    return HttpResponse(pg.bodytext)
