import requests
from csv import DictReader
from datetime import datetime
from django.urls import reverse
from django.db import connection
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.renderers import JSONRenderer
from .serializers import (DepartmentSerializer, BulkDepartmentSerializer,
                          BulkJobSerializer, BulkHiredEmployeeSerializer,
                          HiredEmployeeSerializer)
from .models import Department, Job, HiredEmployee



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


class EmployeesHiredQuarter(APIView):
    def get(self, request, format=None):
        sql = """
            SELECT 
                d.department
                , j.job
                , extract(quarter from h.datetime) as quarter
                , count(*) total
            FROM db_manager_hiredemployee h
            INNER JOIN db_manager_department d on h.department_id_id = d.id
            INNER JOIN db_manager_job j ON h.job_id_id = j.id
            GROUP BY 1,2,3
        """

        with connection.cursor() as cursor:
            cursor.execute(sql)
            hired_employee = cursor.fetchall()

        print(type(hired_employee))
        print(hired_employee)

        serializer = HiredEmployeeSerializer(hired_employee, many=True)
        print("Serializar")
        print(serializer)

        #return Response(serializer)
        return HttpResponse(hired_employee, content_type='application/json')


def post_department_data(request):
    test_url = reverse(
        "departments",
    )
    print("URL")
    url = f"http://0.0.0.0:8000{test_url}"
    print(url)
    with open('./external_files/departments.csv') as f:
        cf = DictReader(f, fieldnames=['id', 'department'])
        for row in cf:
            print("Read File")
            print(row)
            response = requests.post(
                url,
                data={
                    'id': row['id'],
                    'department': row['department']
                }
            )
            print(response.json())
    return HttpResponse("Departments")
