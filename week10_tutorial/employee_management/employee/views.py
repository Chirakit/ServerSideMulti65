import json

from django.db.models import Count, Value
from django.db.models.functions import Concat
from django.http import Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from .forms import EmployeeForm
from .models import *


class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all().order_by("-hire_date")

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
        print(project_id, "1234")
        return JsonResponse({"msg": "ok"})


class ProjectDetailView(View):
    def get(self, request, project_id):
        try:
            project = Project.objects.annotate(
                manager_full_name=Concat('manager__first_name', Value(' '), 'manager__last_name')
            ).get(pk=project_id)
        except Project.DoesNotExist:
            raise Http404("No Project matches the given query.")

        project.due_date = project.due_date.strftime('%Y-%m-%d')
        project.start_date = project.start_date.strftime('%Y-%m-%d')

        context = {'project': project}
        return render(request, 'project_detail.html', context)

    def put(self, request, project_id):
        if 'add_user' in request.path_info:
            project = Project.objects.get(pk=project_id)
            data = json.loads(request.body).get('emp_id')
            employee = Employee.objects.get(pk=data)
            project.staff.add(employee)
            return JsonResponse({'status': 'ok'}, status=200)
        elif 'remove_user' in request.path_info:
            project = Project.objects.get(pk=project_id)
            data = json.loads(request.body).get('emp_id')
            employee = Employee.objects.get(pk=data)
            project.staff.remove(employee)
            return JsonResponse({'status': 'ok'}, status=200)
        elif 'delete_project' in request.path_info:
            project = Project.objects.get(pk=project_id)
            project.delete()
            return JsonResponse({'status': 'ok'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

    def delete(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        project.delete()
        return JsonResponse({'status': 'ok'}, status=200)

class NewEmployee(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'employee_form.html', {'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            birth_date = form.cleaned_data['birth_date']
            hire_date = form.cleaned_data['hire_date']
            salary = form.cleaned_data['salary']
            position = form.cleaned_data['position']
            print(form.cleaned_data)
            Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                birth_date=birth_date,
                hire_date=hire_date,
                salary=salary,
                position=position
            )
        return redirect('employee')