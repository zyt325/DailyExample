from rest_framework import serializers
from apps.hr.models import PeopleViewItd,Departments,Offices

class PeopleViewItdSerializer(serializers.ModelSerializer):
    class Meta:
        model=PeopleViewItd
        fields='__all__'

class PeopleDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['code']
        # fields = '__all__'

class PeopleOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offices
        fields=['code']
        # fields = '__all__'