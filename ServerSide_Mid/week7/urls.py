from django.urls import path

from . import views
urlpatterns = [
    path("", views.EmployeeView.as_view(), name="employees"),
    path("positions/", views.PositionView.as_view(), name="positions"),
    path("projects/", views.ProjectView.as_view(), name="projects"),
    path("projects/<int:project_id>/delete/", views.ProjectView.as_view(), name="project_delete"),
    path("projects/<int:project_id>/", views.ProjectDetailView.as_view(), name="detail"),
    path("projects/<int:project_id>/addStaff/", views.ProjectDetailView.as_view(), name="project_add_staff"),
    path("projects/<int:project_id>/kickStaff/", views.ProjectDetailView.as_view(), name="project_kick_staff"),
]
