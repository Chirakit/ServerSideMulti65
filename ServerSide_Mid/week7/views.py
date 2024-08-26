from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views import View
import json
from .models import *
# Create your views here.

class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, "employee.html", {
            "employees": employees,
            "count": employees.count()
        })

class PositionView(View):
    def get(self, request):
        positions = Position.objects.all()
        return render(request, "position.html", {
            "positions": positions
        })
        
class ProjectView(View):
    def get(self, request):
        return render(request, "project.html", {
            "projects" : Project.objects.all()
        })
    def delete(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        project.delete()
        return HttpResponse('{"delete": true}')

class ProjectDetailView(View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        return render(request, "project_detail.html", {
            "project": project
        })
        
    def put(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        
        content = request.body.decode("utf-8") # ได้ข้อมูลจาก body เป็น bytes เลยต้องทำการ Decode
        content_json = json.loads(content) # แปลงข้อมูลเป็น json
        employee_id = content_json['emp_id']
        project.staff.add(employee_id)
        

        return HttpResponse('{"addStaff": true}')
    
    def delete(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        
        content = request.body.decode("utf-8")
        content_json = json.loads(content)
        employee_id = content_json['emp_id']
        project.staff.remove(employee_id)
        return HttpResponse('{"kickStaff": true}')

# def project_delete(request, project_id):
#     if request.method == "DELETE":
#         project = Project.objects.get(pk=project_id)
#         project.delete()
#         return HttpResponse('{"delete": true}')