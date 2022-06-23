from django.shortcuts import render
from django.http import HttpResponse
import csv
import pandas
import re
# import main as pipe
# Create your views here.
def login(request):
    return render(request,'login.html')
def auth(request):
    if request.method== "POST":
        nm=request.POST.get('username')
        pwd=request.POST.get('password')
        if nm=="ddx1" and pwd=="Demo":
            nc=3
            nonc=0
            #nc - > number of complinet
            #nonc - > number of non complinet
            params={'Nos':nc,'NosNonComliant':nonc}
            
            return render(request,'index.html',params)


def poc_result(request):
    param=[]
    
    file = pandas.read_csv(r'Output/Head of In-House Development and QA, Connected Car - Candidate Brief (1).csv')
    #pandas.set_option('')
    html_string='''
    <html>
        <head><title>PoC Result</tiltle></head>
        <body>
            
        </body>
    </html>
    '''
    file.to_html("templates/result.html",index=False)
    with open(r"templates/result.html", 'r+') as fp:
        # read an store all lines into list
        lines = fp.readlines()
        # move file pointer to the beginning of a file
        fp.seek(0)
        # truncate the file
        fp.truncate()

        # start writing lines except the first line
        # lines[1:] from line 2 to last line
        fp.writelines(lines[1:])
        fp.close()
    with open(r"templates/result.html", 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write("""{% extends 'base.html' %}{% block title %}PoC Test Result{% endblock title %}{% block body %} <div style='background-color:#2E9FF7'><font color='white'><h2><caption>Stack Infrastructure PoC Test Result</caption></h2></font></div>

<h1>MAKE A LIST</h1><table class='table table-striped table-hover'>""" + '\n' + content+"{% endblock body %}")
    
    #with open("templates/result.html",'w') as f:
    #    f.write(html_string.format())
    """ with open(r'Output/Head of In-House Development and QA, Connected Car - Candidate Brief (1).csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            param.append(row) """
        
    return render(request,'result.html')
def overview(request):
    return render(request,'overview.html')