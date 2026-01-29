from django.urls import path

from . import views
from .views import EmployeeView,EmployeeDetailView,EmployeeList
urlpatterns = [    
    path('', EmployeeView.as_view(), name='employee-index'),  
    path('applications/', EmployeeList.as_view(), name='employee-list'),
    path('applications/list/<str:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]