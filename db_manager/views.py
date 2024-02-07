from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import DepartmentSerializer

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
