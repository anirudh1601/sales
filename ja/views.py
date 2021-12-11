from django.shortcuts import render,redirect
from simple_salesforce import Salesforce,format_soql,SalesforceLogin,SFType
import pandas as pd
import json
from .models import Sales,SalesForceModel
from .forms import SalesForm
from django.contrib.auth.models import User

def login(request):
   page = User.objects.get(username=request.user)
   sales = SalesForceModel.objects.get(user=page)
   sf = Salesforce(
      username=sales.username,
      password=sales.password,
      security_token=sales.security_token)
   soq = 'SELECT id,Name From Opportunity'
   query = sf.query(soq)
   sale=None
   #print("record count{0}".format(query['totalSize']))
   isDone=query['done']
   #print(query['records'])
   for q in query['records']:
      sale = Sales.objects.get_or_create(identity=q['Id'],name=q['Name'],user=page)

   abc = Sales.objects.filter(user=page)

   return render(request,'ja/a.html',{'abc':abc})


def retrive(request):
   page = User.objects.get(username=request.user)
   p_form = SalesForm(request.POST or None)
   if request.method=="POST":
      
      if p_form.is_valid():
         instance=p_form.save(commit=False)
         instance.user=page
         instance.save()
         return redirect("login")
   
   return render(request,'ja/form.html',{'form':p_form})

   

   



   

