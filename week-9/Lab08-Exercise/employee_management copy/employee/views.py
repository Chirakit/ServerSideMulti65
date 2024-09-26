import json

from django.db.models import Count, Value
from django.db.models.functions import Concat
from django.db import transaction
from django.http import Http404, JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from company.models import Position
from .forms import EmployeeForm, ProjectForm
from .models import *


class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all().order_by("-hire_date")
        
        for employee in employees:
            employee.position = Position.objects.get(pk=employee.position_id)

        context = {
            "employees": employees,
            "total_employees": len(employees)
        }
        return render(request, "employee.html", context)

class PositionView(View):
    def get(self, request):
        # positions = Position.objects.annotate(num_employees=Count('employee')).order_by('id')

        # context = {
        #     "positions": positions,
        # }
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
            try:
                with transaction.atomic():
                    employee = form.save()
                    location = form.cleaned_data['location']
                    district = form.cleaned_data['district']
                    province = form.cleaned_data['province']
                    postal_code = form.cleaned_data['postal_code']
                    emp_address = EmployeeAddress(employee=employee,location=location, district=district, province=province, postal_code=postal_code)
                    emp_address.save()
            except ObjectDoesNotExist:
                print("Print Fail")    
    
            return redirect('employee')

        return render(request, 'employee_form.html', {'form': form})
    
class NewProject(View):

    def get(self, request):
        form = ProjectForm()
        return render(request, 'project_form.html', {'form': form})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')

        return render(request, 'project_form.html', {'form': form})

class UpdateProject(View):
    def get(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        form = ProjectForm(instance=project)
        return render(request, 'project_detail.html', {'form': form, 'project': project})

    def post(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        form = ProjectForm(request.POST, instance=project)#เราเอาข้อมูลใหม่ไปชี้ใส่ไหน = ใส่ Instance

        if form.is_valid():
            project = form.save()
            return redirect('project_details', project_id=project.id)

        return render(request, 'project_detail.html', {'form': form, 'project': project})
