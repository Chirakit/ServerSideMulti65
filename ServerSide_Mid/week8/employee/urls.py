from django.urls import path

from .views import *
urlpatterns = [
    path("", EmployeeView.as_view(), name="employees"),
    path("positions/", PositionView.as_view(), name="positions"),
    path("projects/", ProjectView.as_view(), name="projects"),
    path("projects/<int:project_id>/", ProjectView.as_view(), name="projectDelete"),
    path("projects/<int:project_id>/detail/", ProjectDetail.as_view(), name="projectDetail"),
    path("projects/<int:project_id>/<int:employee_id>/", ProjectDetail.as_view(), name="projectAction")
]
