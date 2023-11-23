from django.shortcuts import render,redirect
from django.apps import apps
from django import forms
import pyodbc
from .models import EmpForm



# Create your views here.
# def employeelist(request):
#     return render(request,'EmployeeList.html')

def connection(): #establish connection to our sql sserver db
    conn_str=(r'DRIVER={ODBC Driver 17 for SQL Server};'
              r'DATABASE=PythonTrainingDB;'
              r'SERVER=LAPTOP-M3E8PG1T;'
              r'Trusted_Connection=yes;') #Trusted connection is yes and it is using windows login credentials to login
    conn=pyodbc.connect(conn_str)
    return conn

def employeelist(request):
    emplist=[]
    conn=connection()
    cursor=conn.cursor() #Cursor will fetch the data by rows and collumns
    cursor.execute("select * from dbo.Employee")
    for d in cursor.fetchall():
        emplist.append({"EmpID":d[0],"Name":d[1],"Dept":d[2],"Desg":d[3],"Salary":d[4]})
    conn.close()
    return render(request,"EmployeeList.html",{'EL':emplist}) #EL will be accessed inside the html file to diaplay yhe data from emplist

def addemp(request):
    if request.method=="GET":
        return render(request,'AddEmployee.html')
    if request.method=="POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            id=form.cleaned_data.get("id")
            empname=form.cleaned_data.get("empname")
            dept=form.cleaned_data.get("dept")
            desg=form.cleaned_data.get("desg")
            salary=form.cleaned_data.get("salary")
           
            conn=connection()
            cursor=conn.cursor()
            cursor.execute("Insert into dbo.Employee values(?,?,?,?,?)",id,empname,dept,desg,salary)
            conn.commit()
            conn.close()
    return redirect("EmployeeList")

def updateemp(request,id):
    emp=[]
    conn=connection()
    cursor=conn.cursor()
    if request.method=="GET":
        cursor.execute("select * from dbo.Employee where empid=?",id)
        for row in cursor.fetchall():
            emp.append({"id":row[0],"empname":row[1],"dept":row[2],"desg":row[3],"salary":row[4]})
            conn.close()
            return render(request,"AddEmployee.html",{'emp':emp[0]})

    if request.method=="POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            
            empname=form.cleaned_data.get("empname")
            dept=form.cleaned_data.get("dept")
            desg=form.cleaned_data.get("desg")
            salary=form.cleaned_data.get("salary")
            cursor.execute("Update dbo.Employee set name=?,dept=?,desg=?,salary=? where empid=?",empname,dept,desg,salary,id)

            conn.commit()
            conn.close()
            return redirect("EmployeeList")
        
def deleteemp(request,id):
    conn=connection()
    cursor=conn.cursor()
    cursor.execute("delete from dbo.Employee where empid=?",id)
    conn.commit()
    conn.close()
    return redirect("EmployeeList")


    
