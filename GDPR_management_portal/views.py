from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def poc_result(request):
    return render(request,'poc_result.html')
def overview(request):
    return render(request,'overview.html')