from django.shortcuts import render
from django.http import HttpResponse
# import main as pipe
# Create your views here.
def index(request):
    # nc,nonc=pipe.main_pipeline('D:\Infoware\DBI\TEST','D:\Infoware\DBI\Output')
    nc=3
    nonc=0
    #nc - > number of complinet
    #nonc - > number of non complinet
    params={'Nos':nc,'NosNonComliant':nonc}
    
    return render(request,'index.html',params)


def poc_result(request):
    return render(request,'poc_result.html')