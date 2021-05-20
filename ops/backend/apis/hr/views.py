from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from apps.hr.models import PeopleViewItd, Departments, Offices
from apis.hr.serializers import PeopleViewItdSerializer, PeopleDepartmentSerializer, PeopleOfficeSerializer


class PeopleViewItdViewSet(viewsets.ModelViewSet):
    queryset = PeopleViewItd.objects.filter(username__isnull=False)
    serializer_class = PeopleViewItdSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    ordering_fields = ['username', 'category', 'status', 'department_code', 'office_code', 'employee_start_date',
                       'end_date']
    ordering = ['username']
    search_fields = ['$username']
    filterset_fields = ['department_code', 'office_code']


class PeopleDepartmentViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = PeopleDepartmentSerializer
    filter_backends = [OrderingFilter]
    ordering = ['code']


class PeopleOfficeViewSet(viewsets.ModelViewSet):
    queryset = Offices.objects.all()
    serializer_class = PeopleOfficeSerializer
    filter_backends = [OrderingFilter]
    ordering = ['code']
