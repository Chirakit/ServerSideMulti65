from django.urls import path

from . import views
from .views import NewEmployee

urlpatterns = [
    # ex: /polls/
    path("", views.EmployeeView.as_view(), name="employee"),
    path("position/", views.PositionView.as_view(), name="position"),
    path("project/", views.ProjectView.as_view(), name="project"),
    path('project/<int:project_id>/', views.ProjectDetailView.as_view(), name='project_details'),
    path('project/<int:project_id>/add_user', views.ProjectDetailView.as_view(), name='project_details_add_user'),
    path('project/<int:project_id>/remove_user/', views.ProjectDetailView.as_view(),
         name='project_details_remove_user'),
    path('project/<int:project_id>/delete_project/', views.ProjectDetailView.as_view(),
         name='project_details_remove_project'),
    path('new_employee/', NewEmployee.as_view(), name="new_employee"),

]
