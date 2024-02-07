from db_manager.serializers import DepartmentSerializer, JobSerializer


def test_valid_department_serializer():
    valid_serializer_data = {
        "department": "Accounting"
    }
    serializer = DepartmentSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_department_serializer():
    invalid_serializer_data = {

    }
    serializer = DepartmentSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"department": ["This field is required."]}


def test_valid_job_serializer():
    valid_serializer_data = {
        "job": "Accounting"
    }
    serializer = JobSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_job_serializer():
    invalid_serializer_data = {

    }
    serializer = JobSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"job": ["This field is required."]}
