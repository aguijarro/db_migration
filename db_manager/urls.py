from django.urls import path

from .views import (DepartmentList, DepartmentListSerializer, DepartmentBulkListCreateView,
                    JobBulkListCreateView, HiredEmployeeBulkListCreateView)


urlpatterns = [
    path("api/departments/", DepartmentList.as_view(), name="departments"),
    path("api/departments-list-serializer/", DepartmentListSerializer.as_view(), name="departments-list-serializer"),
    path("api/departments-bulk-list-serializer/",
         DepartmentBulkListCreateView.as_view(),
         name="departments-bulk-list-serializer"),
    path("api/job-bulk-list-serializer/",
         JobBulkListCreateView.as_view(),
         name="job-bulk-list-serializer"),
    path("api/hired-employee-bulk-list-serializer/",
         HiredEmployeeBulkListCreateView.as_view(),
         name="hired-employee-bulk-list-serializer"),
]
