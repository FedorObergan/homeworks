import pytest
import random
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student




@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(client, courses_factory):
    # Arrange
    course = courses_factory(_quantity=1)

    # Act
    response = client.get('/api/v1/courses/')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(data) == len(course)
    assert data[0]['name'] == course[0].name

@pytest.mark.django_db
def test_get_several_courses(client, courses_factory):
    # Arrange
    courses = courses_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_courses_filter_id(client, courses_factory):
    # Arrange
    courses = courses_factory(_quantity=8)
    min_id_for_block = courses[0].pk
    random_number = random.randint(0, 7)
    test_id = min_id_for_block + random_number

    # Act
    response = client.get(f'/api/v1/courses/{test_id}/')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert data['id'] == test_id
    assert data['name'] == courses[random_number].name


@pytest.mark.django_db
def test_courses_filter_name(client, courses_factory):
    # Arrange
    courses = courses_factory(_quantity=9)
    random_number = random.randint(0, 8)
    test_name = courses[random_number].name

    # Act
    response = client.get(f'/api/v1/courses/?name={test_name}')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert data[0]['name'] == test_name


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()

    response = client.post('/api/v1/courses/', data={'name': 'ТФКП'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, courses_factory, students_factory):
    students = students_factory(_quantity=3)
    courses = courses_factory(_quantity=7, make_m2m=True, students=students)

    min_id_for_block = courses[0].pk
    random_number = random.randint(0, 6)
    test_id = min_id_for_block + random_number
    new_name = 'Алгебра'
    new_students = students_factory(_quantity=2)
    new_students_list = []
    for student in new_students:
        new_students_list.append(student.pk)
    response = client.patch(f'/api/v1/courses/{test_id}/',
                            data={'name': new_name,
                                  'students': new_students_list})

    assert response.status_code == 200

    response = client.get(f'/api/v1/courses/{test_id}/')
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == new_name
    assert data['students'] == new_students_list


@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    courses = courses_factory(_quantity=5)
    random_number = random.randint(0, 4)
    count = Course.objects.count()

    response = client.delete(f'/api/v1/courses/{courses[random_number].pk}/')

    assert response.status_code == 204
    assert Course.objects.count() == count - 1
