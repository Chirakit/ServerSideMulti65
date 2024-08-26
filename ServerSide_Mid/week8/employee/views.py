from django.shortcuts import render

from django.views import View
from .models import *
from django.http import JsonResponse
# Create your views here.

class EmployeeView(View):
    def get(self, request):
        return render(request, "employee.html", {
            "employees": Employee.objects.all()
        })

class PositionView(View):
    def get(self, request):
        return render(request, "position.html", {
            "positions": Position.objects.all()
        })
        
class ProjectView(View):
    def get(self, request):
        return render(request, "project.html", {
            "projects": Project.objects.all()
        })
    def delete(self, request, project_id):
        Project.objects.get(pk=project_id).delete()
        return JsonResponse({"status": 0})

class ProjectDetail(View):
    def get(self, request, project_id):
        return render(request, "project_detail.html", {
            "project": Project.objects.get(id=project_id)
        })
    def put(self, request, project_id, employee_id):
        Project.objects.get(pk=project_id).staff.add(employee_id)
        return JsonResponse({'status':0})
    def delete(self, request, project_id, employee_id):
        Project.objects.get(pk=project_id).staff.remove(employee_id)
        return JsonResponse({'status':0})