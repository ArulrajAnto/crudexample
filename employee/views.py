# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from employee.forms import EmployeeForm  
from employee.models import Employee 

# Create your views here.  

def emp(request):  
    if request.method == 'POST':  
        form = EmployeeForm(request.POST)  
        if form.is_valid(): 
            form.save()  
            return redirect('show')
    else:
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form}) 


def show(request):  
    employees = Employee.objects.all()  
    return render(request,'show.html',{'employees':employees})  


def edit(request, id): 
    print '1'
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})


def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect('show')  
    return render(request, 'edit.html', {'employee': employee})  

'''
def update(request, id):
    print '34' 
    instance = get_object_or_404(employee, id)
    employee = EmployeeForm(request.POST or None, instance = instance)
    print form.is_valid()
    if form.is_valid():
          form.save()
          return redirect('show')
    else:
        form = EmployeeForm()
    return render(request, 'edit.html', {'employee': employee}) 
 '''

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect('show')  
