from django.shortcuts import render
from django.http import HttpResponse

from .models import Place
from .models import People
# Create your views here.
def fun1(request):
    obj=Place.objects.all()
    obj2=People.objects.all()
    return render(request, "index.html",{'result':obj, 'ppl':obj2})








