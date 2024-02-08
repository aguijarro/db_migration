from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from .serializers import (DepartmentSerializer, BulkDepartmentSerializer,
                          BulkJobSerializer, BulkHiredEmployeeSerializer)
from .models import Department, Job
from datetime import datetime


# Create your views here.


class DepartmentList(APIView):
    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentListSerializer(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(DepartmentListSerializer, self).get_serializer(*args, **kwargs)


class DepartmentBulkListCreateView(generics.ListCreateAPIView):
    """
    # List/Create/Update the relationships between Labels and CaptureSamples

    Required permissions: *Authenticated*, *CaptureLabelValue add*
    """

    serializer_class = BulkDepartmentSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(DepartmentBulkListCreateView, self).get_serializer(
            *args, **kwargs
        )


class JobBulkListCreateView(generics.ListCreateAPIView):
    """
    # List/Create/Update the relationships between Labels and CaptureSamples

    Required permissions: *Authenticated*, *CaptureLabelValue add*
    """

    serializer_class = BulkJobSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(JobBulkListCreateView, self).get_serializer(
            *args, **kwargs
        )


class HiredEmployeeBulkListCreateView(generics.ListCreateAPIView):
    """
    # List/Create/Update the relationships between Labels and CaptureSamples

    Required permissions: *Authenticated*, *CaptureLabelValue add*
    """

    serializer_class = BulkHiredEmployeeSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(HiredEmployeeBulkListCreateView, self).get_serializer(
            *args, **kwargs
        )

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            for item in request.data:
                job = Job.objects.filter(id=item["job_id"]).first()
                department = Department.objects.filter(id=item["department_id"]).first()

                if job and department:
                    item["job_id"] = job.id
                    item["department_id"] = department.id
                    item["datetime"] = datetime.fromisoformat(item["datetime"])
                else:
                    raise ValidationError("Foreign Key does not exist")
        else:
            raise ValidationError("Invalid Input")

        return super(HiredEmployeeBulkListCreateView, self).post(request, *args, **kwargs)