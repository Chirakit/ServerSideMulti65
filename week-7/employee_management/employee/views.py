import json
from django.db.models import Count, Value
from django.db.models.functions import Concat
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import *

class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all()
        context = {
            "employees": employees,
            "total_employees": len(employees)
        }
        return render(request, "employee.html", context)

class PositionView(View):
    def get(self, request):
        positions = Position.objects.annotate(num_employees=Count('employee')).order_by('id')
        context = {
            "positions": positions,
        }
        return render(request, "position.html", context)

class ProjectView(View):
    def get(self, request):
        project = Project.objects.all()
        context = {
            "projects": project,
        }
        return render(request, "project.html", context)
    def delete(self, request, project_id):
        Project.objects.get(pk=project_id).delete()
        return JsonResponse({'status':'ok'}, status=200)

class ProjectdetailView(View):
    def get(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        start = project.start_date.strftime("%Y-%m-%d")
        due = project.due_date.strftime("%Y-%m-%d")
        context = {
            "projects": project,
            "start_date": start,
            "due_date": due,
        }
        return render(request, "project_detail.html", context)
    def put(self, request, project_id, employee_id):
        project = Project.objects.get(pk=project_id)
        employee = Employee.objects.get(pk=employee_id)
        project.staff.add(employee)
        return JsonResponse({'status':'ok'}, status=200)
    def delete(self, request, project_id, employee_id):
        project = Project.objects.get(pk=project_id)
        employee = Employee.objects.get(pk=employee_id)
        project.staff.remove(employee)
        return JsonResponse({'status':'ok'}, status=200)
