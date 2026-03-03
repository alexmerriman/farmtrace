from django.shortcuts import render
from django.http import HttpResponse
from .models import Page

def index(request):
    pg = Page.objects.get(permalink='/')
    title = pg.title
    bodytxt = pg.bodytext
    return render(request, 'index.html')
