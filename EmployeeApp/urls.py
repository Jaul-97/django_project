from django.urls import path
from . import views
urlpatterns=[
    path('',views.employeelist,name="EmployeeList"),
    path('addemp',views.addemp,name='addemp'),
    path('updateemp/<int:id>',views.updateemp,name='updateemp'),
    path('deleteemp/<int:id>',views.deleteemp,name='deleteemp')
    ]