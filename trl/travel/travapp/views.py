from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import team

# Create your views here.
def demo(request):
    obj = team.objects.all()
    return render(request,"index.html",{'result':obj,})
