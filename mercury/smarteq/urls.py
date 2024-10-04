from django.urls import path
from .views import EmployeeView

urlpatterns = [
    path('<int:pk>/', EmployeeView.as_view(), name='Employee'),

]
