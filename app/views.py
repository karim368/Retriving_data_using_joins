from django.shortcuts import render

# Create your views here.

from app.models import *

def equijoins(request):
    EMPOBJ = Emp.objects.select_related('deptno').all()
    d = {'EMPOBJ':EMPOBJ}
    return render(request,'equijoins.html',d)