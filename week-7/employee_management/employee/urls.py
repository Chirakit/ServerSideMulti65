from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.EmployeeView.as_view(), name='employee'),
    path('position/', views.PositionView.as_view(), name='position'),
    path('project/', views.ProjectView.as_view(), name='project'),
    path('project/<int:project_id>/delete/', views.ProjectView.as_view(), name='project'),
    path('project/<int:project_id>/', views.ProjectdetailView.as_view(), name='projectdetail'),
    path('project/<int:project_id>/add/<int:employee_id>/', views.ProjectdetailView.as_view(), name='projectdetail'),
    path('project/<int:project_id>/del/<int:employee_id>/', views.ProjectdetailView.as_view(), name='projectdetail'),
]
