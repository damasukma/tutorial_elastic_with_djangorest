from .models import ProjectApplication
from rest_framework import serializers

class ProjectApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectApplication
        fields = ['project_name', 'path_file', 'status_log']



