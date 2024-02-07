from django.urls import path

from .views import DepartmentList, DepartmentListSerializer


urlpatterns = [
    path("api/departments/", DepartmentList.as_view(), name="departments"),
    path("api/departments-list-serializer/", DepartmentListSerializer.as_view(), name="department-list-serializer"),
]
