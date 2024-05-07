from django.shortcuts import render
from django.http import HttpResponse
from base.forms import ClientForm
# Create your views here.

def index(request):
    if request.method== "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request,"base/dist/index.html")