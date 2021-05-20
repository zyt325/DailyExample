from rest_framework import serializers
from apps.cmdb.models import Host

class HostSerializer(serializers.ModelSerializer):
    map_basicInfo_host = serializers.StringRelatedField(many=True)
    map_label_host = serializers.StringRelatedField(many=True)
    class Meta:
        model=Host
        fields=['id','name','hostname','virtual','map_basicInfo_host','map_label_host']
        # fields='__all__'

