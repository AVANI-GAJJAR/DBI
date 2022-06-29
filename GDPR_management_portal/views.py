from django.shortcuts import render
from django.http import HttpResponse
import csv
import pandas as pd
import re
import pathlib
import csv

import main as pipe
# Create your views here.
def login(request):
    return render(request,'login.html')
def auth(request):
    if request.method== "POST":
        nm=request.POST.get('username')
        pwd=request.POST.get('password')
        if nm=="ddx1" and pwd=="Demo":
            nc,nonc=pipe.main_pipeline(r'/mnt/d/Infoware/DBI/DATA',r'/mnt/d/Infoware/DBI/Output')
            params={'Nos':nc,'NosNonComliant':nonc}
            
            return render(request,'index.html',params)

def overview(request):
    return render(request,'overview.html')

def non_complaint_file_name(request):
    non_complaint_file_name=[]
    html_fl=[]
    for path in pathlib.Path(r'Output').iterdir():
        
        df = pd.read_csv(path)
        if df['Non Compliance Elemets'][0] > 0 :
            non_complaint_file_name.append(path.name)
            q=r'/mnt/d/Infoware/DBI/templates/csv_data//'
            q=q[:-1]
            file = pd.read_csv(path)
            temp=path.name
            s=''
            for i in temp:
                if(i == ' '):
                    s=s+'_'
                else:
                    s=s+i

            s=s[:-4]+'.html'
            c=q+s
            file.to_html(c) 
            html_fl.append(c)
    mylist=zip(non_complaint_file_name,html_fl)

    params={"Comp":mylist}

    return render(request, 'non_comp_name.html',params)

def complaint_file_name(request):
    complaint_file_name=[]
    html_fl=[]
    for path in pathlib.Path(r'Output').iterdir():
        
        df = pd.read_csv(path)
        if df['Non Compliance Elemets'][0] == 0 :
            complaint_file_name.append(path.name)
            q=r'/mnt/d/Infoware/DBI/templates/csv_data//'
            q=q[:-1]
            file = pd.read_csv(path)
            temp=path.name
            s=''
            for i in temp:
                if(i == ' '):
                    s=s+'_'
                else:
                    s=s+i
            s=s[:-4]+'.html'
            c=q+s
            file.to_html(c) 
            html_fl.append(c)
            print(html_fl)
    mylist=zip(complaint_file_name,html_fl)
    params={"Comp":mylist}
    return render(request, 'complaint_files.html',params)
    
def view_table(request):
    liink=request.POST.get('wor','Not Got')

    return render(request,liink)

    
    
